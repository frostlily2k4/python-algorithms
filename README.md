# 🐍 Python Algorithms Library

> A curated collection of classic algorithms and data structures implemented in Python using clean, readable, and well-documented code.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📖 About

This repository is a growing collection of fundamental algorithms and data structures implemented in Python. The goal is to strengthen problem-solving skills, improve understanding of algorithmic concepts, and build a professional GitHub portfolio.

Each implementation focuses on:
- ✅ Clean and readable code
- ✅ Well-documented functions
- ✅ Practical examples
- ✅ Easy-to-understand logic
- ✅ Interview preparation

## 🎯 Goals

This project is designed to:

- 📚 Learn and implement fundamental algorithms and data structures
- 🧠 Strengthen problem-solving and logical thinking skills
- 💻 Practice writing clean, readable, and maintainable Python code
- 🧪 Build reliable implementations with examples and unit tests
- 🎯 Prepare for coding interviews and technical assessments
- 🌟 Showcase consistent learning through a professional GitHub portfolio

## 📂 Project Structure

```text
python-algorithms/
│
├── algorithms/
│   ├── searching/
│   │   └── binary_search.py
│   │
│   ├── sorting/
│   │   ├── merge_sort.py
│   │   ├── quick_sort.py
│   │   └── heap_sort.py
│   │
│   ├── graph/
│   │   ├── bfs.py
│   │   ├── dfs.py
│   │   └── dijkstra.py
│   │
│   ├── trees/
│   │   └── binary_search_tree.py
│   │
│   ├── hashing/
│   │   └── hash_table.py
│   │
│   ├── stack/
│   │   └── stack.py
│   │
│   ├── queue/
│   │   └── queue.py
│   │
│   ├── linked_list/
│   │   └── singly_linked_list.py
│   │
│   ├── doubly_linked_list/
│   │   └── doubly_linked_list.py
│   │
│   └── __init__.py
│
├── tests/
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```
## 🚀 Implemented Algorithms

| Category | Algorithm | Status |
|----------|-----------|:------:|
| 🔍 Searching | Binary Search | ✅ |
| 🔄 Sorting | Merge Sort | ✅ |
| 🔄 Sorting | Quick Sort | ✅ |
| 🔄 Sorting | Heap Sort | ✅ |
| 🌐 Graph | Breadth-First Search (BFS) | ✅ |
| 🌐 Graph | Depth-First Search (DFS) | ✅ |
| 🌐 Graph | Dijkstra's Algorithm | ✅ |
| 🌳 Trees | Binary Search Tree (BST) | ✅ |
| #️⃣ Hashing | Hash Table (Separate Chaining) | ✅ |
| 📦 Stack | Stack (LIFO) | ✅ |
| 📦 Queue | Queue (FIFO) | ✅ |
| 🔗 Linked List | Singly Linked List | ✅ |
| 🔗 Linked List | Doubly Linked List | ✅ |

## 📊 Algorithm Complexity

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|:---------:|:------------:|:----------:|:-----:|
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Breadth-First Search (BFS) | O(V + E) | O(V + E) | O(V + E) | O(V) |
| Depth-First Search (DFS) | O(V + E) | O(V + E) | O(V + E) | O(V) |
| Dijkstra's Algorithm | O((V + E) log V) | O((V + E) log V) | O((V + E) log V) | O(V) |
| Binary Search Tree (BST)* | O(log n) | O(log n) | O(n) | O(n) |
| Hash Table (Separate Chaining)* | O(1) | O(1) | O(n) | O(n) |

> **Note:** The time complexities for Binary Search Tree and Hash Table represent average-case performance. Worst-case performance occurs when the tree becomes unbalanced or when many keys collide in the same hash bucket.

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/frostlily2k4/python-algorithms.git
```

Navigate to the project directory:

```bash
cd python-algorithms
```

(Optional) Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running the Algorithms

Run any algorithm directly using Python.

For example:

```bash
python algorithms/searching/binary_search.py
```

or

```bash
python algorithms/sorting/merge_sort.py
```

or

```bash
python algorithms/graph/bfs.py
```

## 🧪 Running Unit Tests

Run all tests using:

```bash
python -m unittest discover tests
```

## 🛠️ Tech Stack

- **Language:** Python 3
- **Testing:** unittest
- **Version Control:** Git & GitHub
- **IDE:** Visual Studio Code

## 📈 Repository Progress

| Category | Status |
|----------|:------:|
| 🔍 Searching | ✅ Completed |
| 🔄 Sorting | ✅ Completed |
| 🌐 Graph Algorithms | ✅ Completed |
| 🌳 Trees | ✅ Completed |
| #️⃣ Hashing | ✅ Completed |
| 📦 Stack & Queue | ✅ Completed |
| 🔗 Linked Lists | ✅ Completed |
| 💡 Dynamic Programming | 🚧 Coming Soon |
| 🎯 Greedy Algorithms | 🚧 Coming Soon |
| 🔁 Backtracking | 🚧 Coming Soon |
| 🌲 Advanced Trees | 🚧 Coming Soon |

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project, you can:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

Suggestions for new algorithms, optimizations, bug fixes, and documentation improvements are always appreciated.

---

⭐ **If you find this repository helpful, consider giving it a star!**

Happy Coding! 🚀