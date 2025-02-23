# LRU Cache Implementation

## Task

### Step A: Implement LRU Cache

- Implement a **Least Recently Used (LRU) Cache** with **O(1)** time complexity for `get` and `put` operations.
- Implement the `LRUCache` class with:
  - `LRUCache(int capacity)`: Initializes the cache with a given capacity.
  - `get(int key)`: Retrieves the value associated with `key`, or returns `-1` if not found. Logs operation at **INFO** level.
  - `put(int key, int value)`: Inserts or updates the key-value pair. Evicts the **least recently used** item if necessary. Logs operation at **DEBUG** level.

### Step B: Randomized Input Generation & ELK Integration

- Write a script to **randomly generate operations** (`get` and `put`) for testing.
