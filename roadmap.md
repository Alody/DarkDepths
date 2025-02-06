# Roguelike Game Development Roadmap

## Phase 1: Core Mechanics & Infrastructure

### 1. **Dungeon Layout & Node System**
   - Implement a **semi-random node-based** map similar to Peglin.
   - Ensure each node leads to another, forming a branching path.
   - Nodes should be categorized (e.g., enemy encounter, shop, boss).
   - Reveal only a few nodes ahead to maintain suspense.

### 2. **Room Entry System**
   - When entering a node, transition the player into a **room scene**.
   - Each room should load dynamically based on the node type.
   - Implement basic **room variations** (e.g., different layouts, background art).

## Phase 2: Combat System

### 3. **Turn-Based Combat Framework**
   - Establish a **turn order** system.
   - Player should always start on the **left**, enemies on the **right**.
   - Implement **basic attack mechanics** (e.g., damage calculations, hit/miss chance).

### 4. **Combat Menu & Actions**
   - Design a **menu for player actions** (e.g., Attack, Defend, Use Item, Run).
   - Implement UI for **selecting targets** and displaying action results.
   - Allow enemies to take turns and execute **basic AI behavior**.

## Phase 3: Content & Polish

### 5. **Character & Enemy Animations**
   - Implement **idle, attack, hit, and death animations**.
   - Add visual **feedback** for attacks (e.g., flashing, shaking, damage numbers).

### 6. **Enhancements & Additional Features**
   - Introduce **status effects** (e.g., poison, stun, burn).
   - Add different **weapons, abilities, and spells**.
   - Expand enemy variety with **unique attack patterns**.

## Phase 4: Playtesting & Balancing

### 7. **Testing & Feedback**
   - Conduct playtests and tweak mechanics for balance.
   - Optimize performance and fix **bugs/glitches**.
   - Refine **UI/UX** to improve player experience.

## Phase 5: Finalization & Release

### 8. **Final Touches**
   - Add sound effects & music.
   - Implement a **save/load system**.
   - Release a **playable demo** for feedback.
   - Prepare for a full **game release**!

---
### Notes:
- The roadmap is flexible and may evolve based on development needs.
- Focus on **modular, reusable code** for easier expansion.

