tree = ttk.Treeview(table_window, columns=('A', 'B', 'Result', 'type'), show='headings')
tree.heading('A', text='From (A)')
tree.heading('B', text='To (B)')
tree.heading('Result', text='Integration Result')
tree.heading('type', text='Integration type')

tree.pack(pady=20)
