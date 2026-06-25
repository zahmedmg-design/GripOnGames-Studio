# OBS Setup Guide

## 1. Enable OBS WebSocket
OBS 28+ includes WebSocket support.

Go to:
`Tools > WebSocket Server Settings`

Enable:
- Enable WebSocket server
- Server Port: `4455`
- Password: set your own password

Then copy that password into:
`config/config.json`

## 2. Create these OBS scenes
Use exact names:
- Starting Soon
- Pre-Match
- Live Match
- Half-Time
- Full-Time
- Stream Ending

## 3. Add sources to Live Match scene
Use exact source names:
- FM25 Game Capture
- Scoreboard Text
- Clock Text
- Commentary Text

## 4. Add source types
- FM25 Game Capture: Game Capture source
- Scoreboard Text: Text source
- Clock Text: Text source
- Commentary Text: Text source
