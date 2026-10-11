#!/usr/bin/env bash
# Watches one cipher directory and wakes the agent whose turn it is.
# Usage: scripts/watch.sh ciphers/<slug>
# Safe to start repeatedly: a second instance for the same cipher exits at once.
set -u

dir="${1:?usage: scripts/watch.sh ciphers/<slug>}"
dir="${dir%/}"
cd "$(dirname "$0")/.." || exit 1
[ -d "$dir" ] || { echo "no such directory: $dir" >&2; exit 1; }

[ -f watch.conf ] && . ./watch.conf
: "${SOLVER_CMD:=codex exec --full-auto}"
: "${REVIEWER_CMD:=claude -p --allowedTools Read,Write,Edit,Glob,Grep,Bash}"
: "${POLL_SECONDS:=5}"

pidfile="$dir/.watch.pid"
if [ -f "$pidfile" ] && kill -0 "$(cat "$pidfile")" 2>/dev/null; then
  echo "watcher already running for $dir (pid $(cat "$pidfile"))"
  exit 0
fi
echo $$ > "$pidfile"
trap 'rm -f "$pidfile"' EXIT
trap 'exit 0' INT TERM

log() { echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $*" >> "$dir/.watch.log"; }

# Highest n for which the marker <prefix>n exists, or 0.
highest() {
  n="$(ls "$dir" | sed -n "s/^$1\([0-9][0-9]*\)$/\1/p" | sort -n | tail -1)"
  echo "${n:-0}"
}

log "watcher started (pid $$)"
handled=""
while [ ! -e "$dir/FINAL" ]; do
  done_n="$(highest DONE)"
  reviewed_n="$(highest REVIEWED)"

  marker=""
  if [ "$done_n" -gt "$reviewed_n" ]; then
    marker="DONE$done_n" role=reviewer cmd="$REVIEWER_CMD"
  elif [ "$reviewed_n" -gt 0 ]; then
    marker="REVIEWED$reviewed_n" role=solver cmd="$SOLVER_CMD"
  fi

  # Each marker starts an agent once, even if that agent exits without progress.
  if [ -n "$marker" ] && [ "$marker" != "$handled" ]; then
    handled="$marker"
    log "$marker found, starting $role: $cmd"
    $cmd "You are the $role in this repo. The marker $dir/$marker was just created, so it is your turn on the cipher in $dir. Read README.md and follow the instructions for your role." >> "$dir/.watch.log" 2>&1
    log "$role exited with status $?"
  fi

  sleep "$POLL_SECONDS"
done
log "FINAL found, watcher exiting"
