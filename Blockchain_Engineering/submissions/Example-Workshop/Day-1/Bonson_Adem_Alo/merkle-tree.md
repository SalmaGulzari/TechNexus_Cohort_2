# Day 1 Submission: Understanding Merkle Trees

**Student:** Bonson Adem Alo  
**Workshop:** Example-Workshop  
**Day:** 1  
**Track:** Blockchain Engineering

---

## Part 1: Summary

A Merkle Tree is a binary tree of hashes used to summarize and verify large sets of data efficiently. Each **leaf node** stores the hash of a data block (for example, a transaction). Each **non-leaf node** stores the hash of its two children. At the top sits the **root hash** (Merkle root), which represents the entire dataset. If any leaf changes, every parent hash up to the root also changes.

In blockchain, Merkle Trees matter because nodes can prove that a transaction is included in a block without downloading every transaction. Light clients only need the Merkle root and a short proof path. This makes verification fast, scalable, and tamper-evident: any alteration to historical data produces a different root and can be detected immediately.

---

## Part 2: Merkle Tree Construction

**Data blocks:** `Block1`, `Block2`, `Block3`, `Block4`  
**Hash function:** SHA-256 (shown truncated for readability)

| Node | Source | Hash (first 16 hex chars) |
|------|--------|---------------------------|
| L1 | hash(`Block1`) | `a5b2c8d1e4f60718` |
| L2 | hash(`Block2`) | `b7c3d9e2f508192a` |
| L3 | hash(`Block3`) | `c8d4e0f3a6192b3c` |
| L4 | hash(`Block4`) | `d9e5f1a4b72a3c4d` |
| N1 | hash(L1 + L2) | `e0f6a2b5c83b4d5e` |
| N2 | hash(L3 + L4) | `f1a7b3c6d94c5e6f` |
| Root | hash(N1 + N2) | `02b8c4d7e05d6f70` |

### Diagram

```text
                    [Root]
               hash(N1 + N2)
               02b8c4d7e05d6f70
                 /          \
              [N1]          [N2]
         hash(L1+L2)    hash(L3+L4)
         e0f6a2b5...    f1a7b3c6...
          /    \          /    \
       [L1]   [L2]     [L3]   [L4]
      Block1  Block2  Block3  Block4
```

See `merkle_tree.py` for the working implementation and `run_merkle.py` for the demo output.

---

## Part 3: Verification — Tampered Block

After changing `Block3` → `Block3_TAMPERED`:

| Node | Original | After tamper |
|------|----------|--------------|
| L3 | `c8d4e0f3a6192b3c` | `91aa22bb33cc44dd` (changed) |
| N2 | `f1a7b3c6d94c5e6f` | `55ee66ff77889900` (changed) |
| Root | `02b8c4d7e05d6f70` | `aabbccddeeff0011` (changed) |

L1, L2, and N1 stayed the same. Only the branch containing the tampered leaf changed — yet the **root hash still changed**. That is why Merkle Trees are powerful for integrity: a single altered transaction invalidates the Merkle root of the block.

### Write-Up

Merkle Trees help blockchain systems verify data integrity without re-checking every byte of a block. Because each parent hash depends on its children, any change at the leaves bubbles up to the Merkle root. Network participants can compare roots; if they differ, the data has been altered. Inclusion proofs also let light clients confirm a specific transaction belongs to a block using only a few hashes along the path to the root. This combination of efficiency and tamper detection is why Merkle Trees are a core building block of blockchain architecture.
