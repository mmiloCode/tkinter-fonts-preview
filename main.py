from Window import Window

if __name__ == "__main__":
    app = Window()

    cb = app.combobox
    btn_prev = app.btn_prev
    btn_next = app.btn_next

    btn_prev.config(command = app.go_prev)
    btn_next.config(command = app.go_next)

    cb.bind("<<ComboboxSelected>>", lambda e: app.change_font())

    app.mainloop()