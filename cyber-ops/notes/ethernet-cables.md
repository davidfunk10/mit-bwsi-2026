# Straight-Through vs Crossover Cables

Ethernet cables are used to connect devices in a network. Two common types are **straight-through cables** and **crossover cables**.

---

## Straight-Through Cable

A straight-through cable has the **same pinout on both ends**.

This means:
- wire 1 goes to wire 1
- wire 2 goes to wire 2
- and so on

### Used For
Straight-through cables are usually used to connect **different types of devices**.

Examples:
- computer to switch
- computer to router
- switch to router

### Key Idea
A straight-through cable is used when the two devices are designed to transmit and receive on different pins already.

---

## Crossover Cable

A crossover cable has the **transmit and receive wires crossed** between the two ends.

This means some wires switch positions so the sending pins on one device connect to the receiving pins on the other device.

### Used For
Crossover cables are usually used to connect **similar types of devices** directly.

Examples:
- computer to computer
- switch to switch
- router to router

### Key Idea
A crossover cable is used when both devices transmit on the same pins and receive on the same pins, so the wires must cross.

---

## Why the Difference Matters

Devices need to send data from a **transmit (TX)** pin to a **receive (RX)** pin on the other device.

- If the devices already match correctly, use a **straight-through cable**
- If the transmit and receive pins would line up incorrectly, use a **crossover cable**

---

## Simple Rule

- **Straight-through** = connect **different device types**
- **Crossover** = connect **same device types**

---

## Modern Note

Many modern network devices support **Auto-MDI/MDIX**, which allows them to automatically adjust for either cable type.

Because of this, crossover cables are less important today than they were in older networks.

---

## Quick Comparison Table

| Cable Type | Wiring | Common Use |
|-----------|--------|------------|
| Straight-through | same on both ends | different device types |
| Crossover | transmit and receive wires crossed | same device types |

---

## Examples

### Straight-Through
- PC to switch
- PC to router
- switch to router

### Crossover
- PC to PC
- switch to switch
- router to router
