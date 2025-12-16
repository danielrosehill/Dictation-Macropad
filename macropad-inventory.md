# Macropad Inventory

## System Environment

- **Operating System**: Ubuntu 25.10
- **Desktop Environment**: KDE Plasma
- **Display Server**: Wayland
- **Key Remapping Tools**: Input Remapper

## Purpose

This inventory documents all available macropads for speech-to-text dictation workflow optimization. These devices are used for controlling voice recording, transcription, and text formatting operations throughout the day as the primary text input method.

---

## Device Inventory

### 1. Stream Deck Mini

**Type**: Programmable LCD button pad
**Button Count**: 6 buttons (2×3 grid)
**Connectivity**: USB
**Features**:
- LCD displays on each key (customizable icons/labels)
- Software-programmable via Stream Deck software
- Premium build quality

**Layout**:
```
[1] [2] [3]
[4] [5] [6]
```

**Notes**: Top-row buttons (1-3) ideal for most frequent operations due to easier reach. Bottom row (4-6) suitable for secondary functions.

---

### 2. Ali Macropad 1 (6-Key + Knob)

**Type**: QMK-compatible mechanical macropad
**Button Count**: 6 mechanical keys + 1 rotary encoder (knob)
**Connectivity**: USB (HID device)
**Features**:
- QMK firmware support (fully programmable)
- Rotary encoder with push function
- Compact form factor
- Basic HID device

**Layout**:
```
    [Knob]
[1] [2]
[3] [4]
[5] [6]
```

**Notes**: Rotary encoder adds volume/scrolling capability. Knob positioned at top for thumb/index finger access. 2×3 key grid below.

---

### 3. Ali Macropad 2 (21-Key + Knob + Extras)

**Type**: QMK-compatible mechanical macropad with advanced controls
**Button Count**: 21 mechanical keys + 1 large rotary encoder + 4 small directional buttons
**Connectivity**: USB (HID device)
**Features**:
- QMK firmware support
- Large rotary encoder (top-left)
- 4 small directional/navigation buttons (top-right)
- 4×4 main key grid (16 keys)
- Bottom row with 5 smaller keys
- Most complex layout in collection

**Layout**:
```
[Big Knob]    [↑][→]
               [↓][←]

[1]  [2]  [3]  [4]
[5]  [6]  [7]  [8]
[9]  [10] [11] [12]
[13] [14] [15] [16]

[A] [B] [C] [D] [E]
```

**Notes**: Highest button count device. Bottom 5 keys (A-E) are smaller and may be suited for less-frequent operations. Main 4×4 grid ideal for primary workflow functions. Directional buttons could be used for navigation within transcription interface.

---

### 4. Two-Button HID

**Type**: Minimal USB HID button device
**Button Count**: 2 buttons
**Connectivity**: USB (basic HID device)
**Features**:
- Simple two-button footswitch-style design
- QMK-compatible
- Ultra-minimal form factor
- Likely programmable via QMK

**Layout**:
```
[1] [2]
```

**Notes**: Ideal for binary operations (start/stop, record/send). Could be positioned for foot operation or desk-side hand access. Perfect for most critical two functions in workflow.

---

### 5. One-Button HID

**Type**: Single USB HID button device
**Button Count**: 1 button
**Connectivity**: USB (basic HID device)
**Features**:
- Single large button
- QMK-compatible
- Minimal footprint
- Simple HID device

**Layout**:
```
[1]
```

**Notes**: Best suited for the single most critical function (likely "stop and transcribe" combined operation). Could be used as a dedicated "send" button or emergency stop. Ideal for foot operation or prominent desk position.

---

## Key Mapping Strategy

All devices will use **F13-F24** keycodes or custom non-conflicting global shortcuts to avoid interfering with standard Ubuntu/KDE keyboard shortcuts.

**Remapping Tool**: Input Remapper (Wayland-compatible)

---

## Core Functions to Map

Based on dictation workflow, these are the essential functions requiring key assignments:

1. **Start Recording** - Begin new voice recording
2. **Stop Recording** - Stop without sending for transcription
3. **Stop & Transcribe** - Stop recording and immediately send for transcription (combined operation)
4. **Append Recording** - Add to existing recording before transcribing
5. **Send for Transcription** - Send current audio for transcription
6. **Delete Recording** - Discard current recording
7. **Format Selection** - Cycle through or select text format (notes, blog ideas, etc.)

**Secondary Functions**:
- Pause/Resume recording
- Playback recorded audio
- Cancel/Clear
- Navigate between recordings

---

## Device Recommendations by Use Case

### Primary Dictation Control
**Recommended**: Stream Deck Mini or Ali Macropad 2
- Sufficient buttons for all core functions
- Visual feedback (Stream Deck) or extensive layout (Ali 2)

### Minimalist Setup
**Recommended**: Two-Button HID + One-Button HID combination
- Two-button: Start/Stop
- One-button: Stop & Transcribe

### Desk-Side Quick Access
**Recommended**: Ali Macropad 1 (6-key + knob)
- Compact footprint
- Knob for volume/scrolling
- Enough keys for core functions

### Foot Operation
**Recommended**: Two-Button HID or One-Button HID
- Hands-free operation while typing
- Critical start/stop functions

---

## Next Steps

1. Define specific key mappings for each device
2. Configure QMK firmware for HID devices
3. Set up Input Remapper profiles
4. Configure Stream Deck software
5. Test ergonomics and adjust layouts
6. Document final configurations

---

**Last Updated**: 2025-12-16
