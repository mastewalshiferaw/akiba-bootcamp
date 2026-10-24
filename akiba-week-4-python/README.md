# Week 4: Mutability, References, and Memory Model in Python

**Student Name:** Mastewal Getu 
**Assignment:** Week 4 Python Task  
**Organization:** Akiba Technologies  

---

## 1. Assignment Questions & Answers

### Question 1: Mutable and Immutable Objects
- **Difference:** Mutable objects (like lists, dictionaries, sets) can be modified in place after creation without changing their memory address. Immutable objects (like strings, integers, tuples) cannot be altered after creation; any modification produces a brand-new object in memory.
- **Explanation:** In the code demonstration, modifying a list with `.append()` changes the original list directly. Attempting to modify a string directly causes an error, and concatenating strings creates an entirely new string object.

### Question 2: References and Object Identity
- **Output:**
  - `a is b` -> `True`
  - `a is c` -> `False`
  - `a == c` -> `True`
- **Difference between `is` and `==`:** `==` checks for **value equality** (whether contents are identical). `is` checks for **identity** (whether two variables point to the exact same object in memory).
- **Why `a` and `c` have different identities:** Although both lists contain `[10, 20, 30]`, Python allocated two separate list objects at different memory addresses during their creation.

### Question 3: Shared References and Side Effects
- **Predicted Output:** Both `numbers` and `values` output `[1, 2, 3, 4]`.
- **Why it affects both:** The assignment `values = numbers` does not copy the list; it creates a shared reference pointing to the same memory location.
- **Fix:** Creating a shallow copy using slicing `values = numbers[:]` ensures changes to `values` do not affect `numbers`.

### Question 4: Function Arguments and Mutability
- **Output:** `[50, 60, 70, 100]`
- **Why original changes:** Python passes lists by object reference. Modifying `items` via `.append()` directly modifies the caller's list object in memory.
- **Fix:** Copying the list inside the function (`items[:]`) and returning the copy prevents side effects on the original list.

### Question 5: Memory Management and Garbage Collection
- **How it works:** Python uses reference counting along with a cyclic garbage collector. When an object is created, Python tracks how many variables refer to it.
- **What happens when `del` is used:** It removes the variable name and decreases the object's reference counter by 1.
- **Does it always destroy the object?** No. The object is only destroyed if its reference count drops to 0.
- **What happens when an object is no longer referenced?** When reference count is 0, Python's garbage collector automatically reclaims the memory.

---

## 2. Mini-Project Reflection

1. **Why does modifying a shared reference affect the original list?**  
   Because both variable names point to the exact same memory address. Any in-place operation modifies the single shared list object.

2. **Why does modifying the copied list not affect the original list?**  
   Because slicing (`[:]`) creates a separate, independent list object in a new memory address.

3. **What is the difference between equality and identity in Python?**  
   Equality (`==`) evaluates if the data values inside the objects are identical. Identity (`is`) evaluates if both variables point to the exact same memory address (`id()`).

---

## 3. How to Run the Programs

```bash
# Run the questions
python questions.py

# Run the mini-project
python student_marks_manager.py