# FM25 AI Studio v0.1

Windows 11 desktop starter app for Football Manager 25 + OBS Studio broadcast automation.

## What v0.1 includes
- Python desktop app skeleton
- OBS WebSocket connection test
- Scene switching buttons
- Scoreboard/commentary overlay text updater
- 1080p OBS source naming guide
- Config file

## Quick start
1. Install Python 3.11+
2. In OBS: Tools > WebSocket Server Settings > Enable WebSocket server
3. Set OBS WebSocket password in `config/config.json`
4. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
5. Run:
   ```bash
   python app/main.py
   ```

## Recommended OBS scenes
- Starting Soon
- Pre-Match
- Live Match
- Half-Time
- Full-Time
- Stream Ending

## Recommended OBS source names
Use these exact names for automation:
- `FM25 Game Capture`
- `Scoreboard Text`
- `Clock Text`
- `Commentary Text`
- `Goal Banner`
- `Card Banner`
