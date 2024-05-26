import tkinter as tk
from tkinter import scrolledtext, filedialog, font, ttk

def remove_redundant_groups(groups):
    """
    Remove redundant groups from a list of groups. """
    unique_groups = []
    for group in groups:
        if group not in unique_groups:
            unique_groups.append(group)
    return unique_groups

def get_new_groups():
    """ Get the new groups corresponding to the input old groups. """
    old_groups = input_text.get("1.0", "end-1c").split(",")
    old_groups = [group.strip() for group in old_groups]
    new_groups = []
    for old_group in old_groups:
        if old_group in old_to_new_groups:
            new_groups.extend(old_to_new_groups[old_group])
    unique_new_groups = remove_redundant_groups(new_groups)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", "| ".join(unique_new_groups))

def load_old_to_new_groups():
    """ Load the old-to-new groups mapping from a file. """
    file_path = filedialog.askopenfilename(title="Select Old to New Groups File")
    if file_path:
        global old_to_new_groups
        old_to_new_groups = {}
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if ":" in line:
                    old_group, new_groups_str = line.split(":", 1)
                    new_groups = [group.strip() for group in new_groups_str.split(",")]
                    old_to_new_groups[old_group] = new_groups

def convert_old_to_new_format():
    """ Convert the old group format to the new format. """
    old_format_groups = old_format_input.get("1.0", "end-1c").split("\n")
    old_format_groups = [group.strip() for group in old_format_groups]
    new_format_groups = []
    for old_format_group in old_format_groups:
        if old_format_group:
            cn_value = old_format_group.split(",")[0].split("=")[1]
            if cn_value != "jsam-ogr-superuser":  # Exclude "jsam-ogr-superuser" group
                new_format_groups.append(cn_value)
    new_format_output.delete("1.0", "end")
    new_format_output.insert("1.0", ",".join(new_format_groups))

def copy_text(text_widget):
    """ Copy the content of a text widget to the clipboard. """
    text = text_widget.get("1.0", "end-1c")
    window.clipboard_clear()
    window.clipboard_append(text)

def clear_text(text_widget):
    """ Clear the content of a text widget. """
    text_widget.delete("1.0", "end")

def clear_all_fields():
    """ Clear all text fields. """
    clear_text(old_format_input)
    clear_text(new_format_output)
    clear_text(input_text)
    clear_text(output_text)

# main window
window = tk.Tk()
window.title("Old to New Groups Converter")
window.geometry("600x850")

window.configure(bg="#F0F0F0")

# style for the text widgets
style = ttk.Style()
style.configure("Custom.TEntry", foreground="white", background="black", padding=5, relief="flat")
style.configure("Custom.Text", foreground="white", background="black", padding=5, relief="flat")

# custom font
custom_font = font.Font(family="Helvetica", size=12)

old_format_input_label = tk.Label(window, text="Enter old format groups (one per line):", bg="#F0F0F0", fg="#333333", font=custom_font)
old_format_input_label.pack(pady=10)

old_format_input = scrolledtext.ScrolledText(window, height=5, width=100, font=custom_font, wrap="word")
old_format_input.pack(padx=20)

old_format_input_buttons_frame = tk.Frame(window, bg="#F0F0F0")
old_format_input_buttons_frame.pack()

copy_old_format_input_button = tk.Button(old_format_input_buttons_frame, text="Copy", command=lambda: copy_text(old_format_input), bg="#4285F4", fg="#333333", font=custom_font, relief="raised", borderwidth=3, activebackground="#3367D6", activeforeground="#FFFFFF")
copy_old_format_input_button.pack(side=tk.LEFT, padx=5)

clear_old_format_input_button = tk.Button(old_format_input_buttons_frame, text="Clear", command=lambda: clear_text(old_format_input), bg="#4285F4", fg="#333333", font=custom_font, relief="raised", borderwidth=3, activebackground="#3367D6", activeforeground="#FFFFFF")
clear_old_format_input_button.pack(side=tk.LEFT, padx=5)

convert_button = tk.Button(window, text="Convert to New Format", command=convert_old_to_new_format, bg="#4285F4", fg="#333333", font=custom_font, relief="raised", borderwidth=3, activebackground="#3367D6", activeforeground="#FFFFFF")
convert_button.pack(pady=10)

new_format_output_label = tk.Label(window, text="New format groups:", bg="#F0F0F0", fg="#000080", font=custom_font)
new_format_output_label.pack()

new_format_output = scrolledtext.ScrolledText(window, height=5, width=100, font=custom_font, wrap="word")
new_format_output.pack(padx=20)

new_format_output_buttons_frame = tk.Frame(window, bg="#F0F0F0")
new_format_output_buttons_frame.pack()

copy_new_format_output_button = tk.Button(new_format_output_buttons_frame, text="Copy", command=lambda: copy_text(new_format_output), bg="#4285F4", fg="#333333", font=custom_font, relief="raised", borderwidth=3, activebackground="#3367D6", activeforeground="#FFFFFF")
copy_new_format_output_button.pack(side=tk.LEFT, padx=5)

clear_new_format_output_button = tk.Button(new_format_output_buttons_frame, text="Clear", command=lambda: clear_text(new_format_output), bg="#4285F4", fg="#333333", font=custom_font, relief="raised", borderwidth=3, activebackground="#3367D6", activeforeground="#FFFFFF")
clear_new_format_output_button.pack(side=tk.LEFT, padx=5)

load_mapping_button = tk.Button(window, text="Load Old to New Groups Mapping", command=load_old_to_new_groups, bg="#4285F4", fg="#333333", font=custom_font, relief="raised", borderwidth=3, activebackground="#3367D6", activeforeground="#FFFFFF")
load_mapping_button.pack(pady=10)

input_label = tk.Label(window, text="Enter old groups (comma-separated):", bg="#F0F0F0", fg="#333333", font=custom_font)
input_label.pack(pady=10)

input_text = scrolledtext.ScrolledText(window, height=5, width=100, font=custom_font, wrap="word")
input_text.pack(padx=20)

input_buttons_frame = tk.Frame(window, bg="#F0F0F0")
input_buttons_frame.pack()

copy_input_button = tk.Button(input_buttons_frame, text="Copy", command=lambda: copy_text(input_text), bg="#4285F4", fg="#333333", font=custom_font, relief="raised", borderwidth=3, activebackground="#3367D6", activeforeground="#FFFFFF")
copy_input_button.pack(side=tk.LEFT, padx=5)

clear_input_button = tk.Button(input_buttons_frame, text="Clear", command=lambda: clear_text(input_text), bg="#4285F4", fg="#333333", font=custom_font, relief="raised", borderwidth=3, activebackground="#3367D6", activeforeground="#FFFFFF")
clear_input_button.pack(side=tk.LEFT, padx=5)

get_new_groups_button = tk.Button(window, text="Get New Groups", command=get_new_groups, bg="#4285F4", fg="#333333", font=custom_font, relief="raised", borderwidth=3, activebackground="#3367D6", activeforeground="#FFFFFF")
get_new_groups_button.pack(pady=10)

output_label = tk.Label(window, text="New groups:", bg="#F0F0F0", fg="#000080", font=custom_font)
output_label.pack()

output_text = scrolledtext.ScrolledText(window, height=5, width=100, font=custom_font, wrap="word")
output_text.pack(padx=20)

output_buttons_frame = tk.Frame(window, bg="#F0F0F0")
output_buttons_frame.pack()

copy_output_button = tk.Button(output_buttons_frame, text="Copy", command=lambda: copy_text(output_text), bg="#4285F4", fg="#333333", font=custom_font, relief="raised", borderwidth=3, activebackground="#3367D6", activeforeground="#FFFFFF")
copy_output_button.pack(side=tk.LEFT, padx=5)

clear_output_button = tk.Button(output_buttons_frame, text="Clear", command=lambda: clear_text(output_text), bg="#4285F4", fg="#333333", font=custom_font, relief="raised", borderwidth=3, activebackground="#3367D6", activeforeground="#FFFFFF")
clear_output_button.pack(side=tk.LEFT, padx=5)

# button to clear all fields
clear_all_fields_button = tk.Button(window, text="Clear All Fields", command=clear_all_fields, bg="#FF0000", fg="black", font=custom_font, relief="raised", borderwidth=3, activebackground="#CC0000", activeforeground="#FFFFFF")
clear_all_fields_button.pack(pady=10)


window.mainloop()