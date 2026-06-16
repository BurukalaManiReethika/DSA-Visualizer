import tkinter as tk
from tkinter import messagebox

# Data Structures
stack = []
queue = []
linked_list = []

# ---------------- STACK ---------------- #
def push_stack():
    value = entry.get()
    if value:
        stack.append(value)
        update_stack()
        entry.delete(0, tk.END)

def pop_stack():
    if stack:
        stack.pop()
        update_stack()
    else:
        messagebox.showwarning("Stack", "Stack is Empty!")

def update_stack():
    stack_list.delete(0, tk.END)
    for item in reversed(stack):
        stack_list.insert(tk.END, item)

# ---------------- QUEUE ---------------- #
def enqueue():
    value = entry.get()
    if value:
        queue.append(value)
        update_queue()
        entry.delete(0, tk.END)

def dequeue():
    if queue:
        queue.pop(0)
        update_queue()
    else:
        messagebox.showwarning("Queue", "Queue is Empty!")

def update_queue():
    queue_list.delete(0, tk.END)
    for item in queue:
        queue_list.insert(tk.END, item)

# ---------------- LINKED LIST ---------------- #
def insert_node():
    value = entry.get()
    if value:
        linked_list.append(value)
        update_linked_list()
        entry.delete(0, tk.END)

def delete_node():
    value = entry.get()

    if value in linked_list:
        linked_list.remove(value)
        update_linked_list()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Linked List", "Node Not Found!")

def update_linked_list():
    linked_listbox.delete(0, tk.END)

    display = " → ".join(linked_list)

    if linked_list:
        display += " → NULL"

    linked_listbox.insert(tk.END, display)

# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("DSA Visualizer")
root.geometry("900x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="DSA Visualizer",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=20)

# Stack Section
stack_frame = tk.LabelFrame(
    frame,
    text="Stack",
    padx=10,
    pady=10
)
stack_frame.grid(row=0, column=0, padx=20)

stack_list = tk.Listbox(stack_frame, width=20, height=10)
stack_list.pack()

tk.Button(
    stack_frame,
    text="Push",
    command=push_stack
).pack(side=tk.LEFT, padx=5)

tk.Button(
    stack_frame,
    text="Pop",
    command=pop_stack
).pack(side=tk.LEFT)

# Queue Section
queue_frame = tk.LabelFrame(
    frame,
    text="Queue",
    padx=10,
    pady=10
)
queue_frame.grid(row=0, column=1, padx=20)

queue_list = tk.Listbox(queue_frame, width=20, height=10)
queue_list.pack()

tk.Button(
    queue_frame,
    text="Enqueue",
    command=enqueue
).pack(side=tk.LEFT, padx=5)

tk.Button(
    queue_frame,
    text="Dequeue",
    command=dequeue
).pack(side=tk.LEFT)

# Linked List Section
linked_frame = tk.LabelFrame(
    frame,
    text="Linked List",
    padx=10,
    pady=10
)
linked_frame.grid(row=0, column=2, padx=20)

linked_listbox = tk.Listbox(
    linked_frame,
    width=35,
    height=10
)
linked_listbox.pack()

tk.Button(
    linked_frame,
    text="Insert",
    command=insert_node
).pack(side=tk.LEFT, padx=5)

tk.Button(
    linked_frame,
    text="Delete",
    command=delete_node
).pack(side=tk.LEFT)

root.mainloop()
