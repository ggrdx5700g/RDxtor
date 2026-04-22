# RDxtor - Tor Proxy Configuration Tool

## Overview
**RDxtor** is a Python-based utility tool that automates the setup and configuration of Tor proxy access through Proxychains on Linux systems.

---

## What This Tool Does
- Enables anonymous Tor browsing by configuring proxychains
- Simplifies Tor proxy setup (setup script)
- Provides cleanup functionality to reset proxy settings (teardown script)

---

## Installation & Setup

### Prerequisites
- Python 3.x installed
- Proxychains installed on your system
- Firefox browser (for proxy list selection)
- Linux/Unix-based operating system

### Step 1: Grant Execution Permissions

Make both Python scripts executable:

```bash
chmod +x rdxtor.py
chmod +x rdxtorantidot.py
```

---

## Usage

### Step 1: Enable Tor Proxy (Setup)

Run the setup script:

```bash
python3 rdxtor.py
```

**What this does:**
- Configures Proxychains for Tor routing

### Step 2: Configure Proxychains Settings

Manually configure the following in your proxychains config file:

1. **Enable strict_chain mode:**
   - Comment out `dynamic_chain`
   - Comment `strict_chain`

2. **Disable proxy DNS:**
   - Comment out `proxy_dns` option

3. **Add Proxy IPs:**
   - Search for proxy lists in Firefox
   - Add proxy entries in the format: `protocol ip_address port`
   - Example: `socks5 127.0.0.1 9050`
   - You can add multiple proxies

4. **Save Changes:**
   - Press `Ctrl+S` to save
   - Click the close button (X icon)

**Tip:** Use DuckDuckGo for private searches within Firefox

---

## Step 3: Disable Tor Proxy (Cleanup)

After finished using Tor, run the cleanup script:

```bash
python3 rdxtoranti.py
```

**What this does:**
- Resets all Proxychains configuration changes
- Restores previous proxy settings

**Steps to reset manually:**
1. Revert all changes you made in the Proxychains config
2. Restore original settings
3. Press `Ctrl+S` to save
4. Click the close button (X icon)

---

## Quick Start Guide

| Step | Action |
|------|--------|
| 1 | Make scripts executable: `chmod +x rdxtor.py rdxtorantidot.py` |
| 2 | Run setup: `python3 rdxtor.py` |
| 3 | Configure proxychains (strict_chain, add proxies) |
| 4 | Use Tor anonymously |
| 5 | Run cleanup: `python3 rdxtorantidot.py` |
| 6 | Reset proxychains config |

---

## File Structure

```
RDxtor/
├── rdxtor.py              # Setup/Enable Tor proxy script
├── rdxtorantidot.py       # Cleanup/Disable Tor proxy script
└── README.md              # Documentation
```

---

## Security & Privacy Notes

- ✅ Use this for **legitimate privacy purposes only**
- ✅ Always remember to run cleanup script when done
- ✅ Consider using DuckDuckGo or other privacy-focused search engines
- ⚠️ Ensure you have proper permissions to modify system proxy settings
- ⚠️ Be aware of local laws regarding proxy/Tor usage

---

## Requirements

- **Language:** Python 3.x
- **Dependencies:** Proxychains
- **OS:** Linux/Unix-based systems
- **Permissions:** Root or sudo access (for proxychains configuration)

---

## Author & License

Created by: **ggrdx5700g**

Language: **100% Python**

---

## Support & Troubleshooting

**Issue: Permission denied when running script**
- Solution: Run `chmod +x rdxtor.py rdxtorantidot.py`

**Issue: Proxychains not found**
- Solution: Install proxychains: `sudo apt-get install proxychains` (Debian/Ubuntu)

**Issue: Proxy connections failing**
- Solution: Verify proxy format (protocol, IP, port) in proxychains config

---
