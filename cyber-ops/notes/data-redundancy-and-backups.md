# Data Redundancy & Backups

## Overview
Data redundancy and backups are both used to protect data, but they serve different purposes. Redundancy focuses on **keeping systems running**, while backups focus on **recovering lost data**.

---

## RAID (Redundant Array of Independent Disks)

**Definition:**
Redundant Array of Inexpensive (Independent) Disks is a means of orchestrating reliable mass file storage. The connotation is that these disks are linked together with a controller. These disks work actively together with the goal of data recoverability and reliability of mass storage.

When you "RAID" multiple hard drives together, you typically lose usable storage.

**Example:**
- 2 × 1TB drives in RAID 1 → only **1TB usable**
- Data is mirrored (copied 1:1)
- If one drive fails → data is safe
- If both drives fail → **data is lost**

---

## Common RAID Levels

### RAID 0 (Striping)
- Splits data across drives
- ✅ Very fast
- ❌ No redundancy (if one drive fails → all data lost)

### RAID 1 (Mirroring)
- Copies data across drives
- ✅ High reliability
- ❌ 50% storage efficiency

### RAID 5 (Striping + Parity)
- Uses 3+ drives
- Data + parity distributed
- ✅ Can survive 1 drive failure
- ⚖️ Balanced performance + redundancy

### RAID 10 (1+0)
- Combination of RAID 1 and RAID 0
- ✅ Fast + redundant
- ❌ Requires more drives

---

## ⚠️ Important Concept

**RAID is NOT backup**

RAID protects against **hardware failure**, not:
- Accidental deletion
- Malware/ransomware
- File corruption
- User error

---

## Backup

**Definition:**
Backing up is saving your files to **separate, independent locations** so they can be recovered if lost.

---

## 3-2-1 Rule

A common best practice:
- **3 copies** of your data
- **2 different storage types** (e.g., HDD + cloud)
- **1 offsite backup**

---

## Types of Backups

### Full Backup
- Copies all data
- ✅ Simple restore
- ❌ Takes most time and storage

### Incremental Backup
- Saves changes since last backup (any type)
- ✅ Fast, efficient
- ❌ Slower restore (needs multiple backups)

### Differential Backup
- Saves changes since last full backup
- ⚖️ Balance between speed and restore simplicity

---

## RAID vs Backup

| Feature | RAID | Backup |
|--------|------|--------|
| Purpose | Uptime / reliability | Data recovery |
| Protects against drive failure | ✅ | ✅ |
| Protects against deletion | ❌ | ✅ |
| Protects against malware | ❌ | ✅ |
| Storage efficiency | Often reduced | Depends on method |
| Location | Same system | Separate location |

---

## Key Takeaways

- RAID improves **system reliability**, not true data safety
- Backups protect against **real-world data loss scenarios**
- You should always use **both RAID and backups together**
- Follow the **3-2-1 rule** for maximum protection
