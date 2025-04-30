import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys
import os
# تحديد مسار الموارد للمكتبات
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)
class DataAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.data = None
        self.file_path = None
        self.dark_mode = False
        self.language = "arabic"  # Default language
        
        # Language dictionary
        self.lang_dict = {
            "english": {
                "title": "Data Analysis Tool",
                "load_csv": "Load CSV File",
                "no_file": "No file loaded",
                "choose_file": "Choose File",
                "clean_ops": "Data Cleaning",
                "remove_dup": "Remove Duplicates",
                "remove_null": "Remove Null Values",
                "fill_null": "Fill Null Values",
                "stats": "Statistics",
                "show_stats": "Show Statistics",
                "show_info": "Show Data Info",
                "quick_view": "Quick View",
                "export": "Export Data",
                "change_lang": "Switch to Arabic",
                "toggle_theme": "Dark Mode",
                "data_tab": "Data",
                "success": "Success",
                "warning": "Warning",
                "error": "Error",
                "file_loaded": "File loaded successfully!",
                "duplicates_removed": " duplicates removed",
                "nulls_removed": " rows with null values removed",
                "nulls_filled": "Null values filled successfully",
                "stats_calculated": "Statistics calculated",
                "data_info": "Data information",
                "rows": "Rows: ",
                "columns": "Columns: ",
                "cols_list": "Columns list:",
                "quick_view_gen": "Quick view generated",
                "data_exported": "Data exported successfully",
                "no_data": "No data loaded!",
                "load_error": "Failed to load file: ",
                "export_error": "Failed to export data: "
            },
            "arabic": {
                "title": "أداة تحليل البيانات",
                "load_csv": "تحميل ملف CSV",
                "no_file": "لم يتم تحميل أي ملف",
                "choose_file": "اختر ملف",
                "clean_ops": "تنظيف البيانات",
                "remove_dup": "إزالة التكرارات",
                "remove_null": "إزالة القيم الفارغة",
                "fill_null": "ملء القيم الفارغة",
                "stats": "الإحصائيات",
                "show_stats": "عرض الإحصائيات",
                "show_info": "عرض معلومات البيانات",
                "quick_view": "عرض سريع",
                "export": "تصدير البيانات",
                "change_lang": "التبديل للإنجليزية",
                "toggle_theme": "الوضع الليلي",
                "data_tab": "البيانات",
                "success": "نجاح",
                "warning": "تحذير",
                "error": "خطأ",
                "file_loaded": "تم تحميل الملف بنجاح!",
                "duplicates_removed": " صف مكرر تمت إزالته",
                "nulls_removed": " صف يحتوي على قيم فارغة تمت إزالته",
                "nulls_filled": "تم ملء القيم الفارغة بنجاح",
                "stats_calculated": "تم حساب الإحصائيات",
                "data_info": "معلومات البيانات",
                "rows": "عدد الصفوف: ",
                "columns": "عدد الأعمدة: ",
                "cols_list": "قائمة الأعمدة:",
                "quick_view_gen": "تم إنشاء العرض السريع",
                "data_exported": "تم تصدير البيانات بنجاح",
                "no_data": "لم يتم تحميل أي بيانات!",
                "load_error": "فشل تحميل الملف: ",
                "export_error": "فشل تصدير البيانات: "
            }
        }
        
        # Themes setup
        self.themes = {
            "light": {
                "bg": "#f0f2f5",
                "fg": "#333333",
                "button_bg": "#4a90e2",
                "button_fg": "#ffffff",
                "button_active": "#3a7bc8",
                "frame_bg": "#ffffff",
                "text_bg": "#ffffff",
                "text_fg": "#333333",
                "highlight": "#4a90e2",
                "tab_bg": "#ffffff",
                "tab_fg": "#333333",
                "header_bg": "#4a90e2",
                "header_fg": "#ffffff",
                "plot_bg": "#ffffff",
                "plot_fg": "#333333"
            },
            "dark": {
                "bg": "#1e1e1e",
                "fg": "#e0e0e0",
                "button_bg": "#5da5ff",
                "button_fg": "#ffffff",
                "button_active": "#4d8be6",
                "frame_bg": "#2d2d2d",
                "text_bg": "#252525",
                "text_fg": "#e0e0e0",
                "highlight": "#5da5ff",
                "tab_bg": "#252525",
                "tab_fg": "#e0e0e0",
                "header_bg": "#1a3d66",
                "header_fg": "#ffffff",
                "plot_bg": "#252525",
                "plot_fg": "#e0e0e0"
            }
        }
        self.current_theme = self.themes["light"]
        
        # Fonts setup
        self.fonts = {
            "title": ("Arial", 14, "bold"),
            "button": ("Arial", 12),
            "text": ("Arial", 11),
            "header": ("Arial", 12, "bold")
        }
        
        # Window setup
        self.setup_window()
        self.create_widgets()
        self.apply_theme()
        self.update_language()
    
    def setup_window(self):
        self.root.title(self.lang_dict[self.language]["title"])
        self.root.geometry("1100x750")
        self.root.minsize(1000, 700)
        self.root.configure(bg=self.current_theme['bg'])
    
    def update_language(self):
        lang = self.lang_dict[self.language]
        self.root.title(lang["title"])
        
        # Update all widgets with new language
        if hasattr(self, 'file_frame'):
            self.file_frame.config(text=lang["load_csv"])
            self.file_label.config(text=lang["no_file"])
            self.browse_btn.config(text=lang["choose_file"])
            self.clean_frame.config(text=lang["clean_ops"])
            self.remove_dup_btn.config(text=lang["remove_dup"])
            self.remove_null_btn.config(text=lang["remove_null"])
            self.fill_null_btn.config(text=lang["fill_null"])
            self.stats_frame.config(text=lang["stats"])
            self.show_stats_btn.config(text=lang["show_stats"])
            self.show_info_btn.config(text=lang["show_info"])
            self.quick_view_btn.config(text=lang["quick_view"])
            self.export_btn.config(text=lang["export"])
            self.lang_btn.config(text=lang["change_lang"])
            self.theme_btn.config(text=lang["toggle_theme"])
            self.notebook.tab(0, text=lang["data_tab"])
            self.notebook.tab(1, text=lang["quick_view"])
    
    def toggle_language(self):
        self.language = "arabic" if self.language == "english" else "english"
        self.update_language()
    
    def create_widgets(self):
        # Main container
        main_container = tk.Frame(self.root, bg=self.current_theme['bg'])
        main_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Left panel
        left_panel = tk.Frame(main_container, width=250, bg=self.current_theme['frame_bg'])
        left_panel.pack(side="left", fill="y", padx=5, pady=5)
        left_panel.pack_propagate(False)
        
        # File frame
        self.file_frame = tk.LabelFrame(left_panel, text=self.lang_dict[self.language]["load_csv"],
                                      bg=self.current_theme['frame_bg'], fg=self.current_theme['fg'],
                                      font=self.fonts["header"])
        self.file_frame.pack(fill="x", pady=5, padx=5)
        
        self.file_label = tk.Label(self.file_frame, text=self.lang_dict[self.language]["no_file"],
                                 bg=self.current_theme['frame_bg'], fg=self.current_theme['fg'],
                                 font=self.fonts["text"])
        self.file_label.pack(side="top", fill="x", padx=5, pady=5)
        
        self.browse_btn = tk.Button(self.file_frame, text=self.lang_dict[self.language]["choose_file"],
                                  command=self.load_file,
                                  bg=self.current_theme['button_bg'], fg=self.current_theme['button_fg'],
                                  font=self.fonts["button"])
        self.browse_btn.pack(fill="x", padx=5, pady=5)
        
        # Clean operations frame
        self.clean_frame = tk.LabelFrame(left_panel, text=self.lang_dict[self.language]["clean_ops"],
                                       bg=self.current_theme['frame_bg'], fg=self.current_theme['fg'],
                                       font=self.fonts["header"])
        self.clean_frame.pack(fill="x", pady=5, padx=5)
        
        self.remove_dup_btn = tk.Button(self.clean_frame, text=self.lang_dict[self.language]["remove_dup"],
                                      command=self.remove_duplicates,
                                      bg=self.current_theme['button_bg'], fg=self.current_theme['button_fg'],
                                      font=self.fonts["button"])
        self.remove_dup_btn.pack(fill="x", padx=5, pady=2)
        
        self.remove_null_btn = tk.Button(self.clean_frame, text=self.lang_dict[self.language]["remove_null"],
                                       command=self.remove_null,
                                       bg=self.current_theme['button_bg'], fg=self.current_theme['button_fg'],
                                       font=self.fonts["button"])
        self.remove_null_btn.pack(fill="x", padx=5, pady=2)
        
        self.fill_null_btn = tk.Button(self.clean_frame, text=self.lang_dict[self.language]["fill_null"],
                                     command=self.fill_null,
                                     bg=self.current_theme['button_bg'], fg=self.current_theme['button_fg'],
                                     font=self.fonts["button"])
        self.fill_null_btn.pack(fill="x", padx=5, pady=2)
        
        # Stats frame
        self.stats_frame = tk.LabelFrame(left_panel, text=self.lang_dict[self.language]["stats"],
                                       bg=self.current_theme['frame_bg'], fg=self.current_theme['fg'],
                                       font=self.fonts["header"])
        self.stats_frame.pack(fill="x", pady=5, padx=5)
        
        self.show_stats_btn = tk.Button(self.stats_frame, text=self.lang_dict[self.language]["show_stats"],
                                      command=self.show_stats,
                                      bg=self.current_theme['button_bg'], fg=self.current_theme['button_fg'],
                                      font=self.fonts["button"])
        self.show_stats_btn.pack(fill="x", padx=5, pady=2)
        
        self.show_info_btn = tk.Button(self.stats_frame, text=self.lang_dict[self.language]["show_info"],
                                     command=self.show_info,
                                     bg=self.current_theme['button_bg'], fg=self.current_theme['button_fg'],
                                     font=self.fonts["button"])
        self.show_info_btn.pack(fill="x", padx=5, pady=2)
        
        self.quick_view_btn = tk.Button(self.stats_frame, text=self.lang_dict[self.language]["quick_view"],
                                      command=self.show_quick_view,
                                      bg=self.current_theme['button_bg'], fg=self.current_theme['button_fg'],
                                      font=self.fonts["button"])
        self.quick_view_btn.pack(fill="x", padx=5, pady=2)
        
        # Export button
        self.export_btn = tk.Button(left_panel, text=self.lang_dict[self.language]["export"],
                                   command=self.export_data,
                                   bg=self.current_theme['button_bg'], fg=self.current_theme['button_fg'],
                                   font=self.fonts["button"])
        self.export_btn.pack(fill="x", padx=5, pady=10)
        
        # Language button
        self.lang_btn = tk.Button(left_panel, text=self.lang_dict[self.language]["change_lang"],
                                 command=self.toggle_language,
                                 bg=self.current_theme['button_bg'], fg=self.current_theme['button_fg'],
                                 font=self.fonts["button"])
        self.lang_btn.pack(fill="x", padx=5, pady=5)
        
        # Theme button
        self.theme_btn = tk.Button(left_panel, text=self.lang_dict[self.language]["toggle_theme"],
                                  command=self.toggle_theme,
                                  bg=self.current_theme['button_bg'], fg=self.current_theme['button_fg'],
                                  font=self.fonts["button"])
        self.theme_btn.pack(fill="x", padx=5, pady=5)
        
        # Right panel
        right_panel = tk.Frame(main_container, bg=self.current_theme['bg'])
        right_panel.pack(side="right", fill="both", expand=True, padx=5, pady=5)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(right_panel)
        self.notebook.pack(fill="both", expand=True)
        
        # Data tab
        self.data_tab = tk.Frame(self.notebook, bg=self.current_theme['frame_bg'])
        self.notebook.add(self.data_tab, text=self.lang_dict[self.language]["data_tab"])
        
        # Text widget with scrollbar
        scrollbar = tk.Scrollbar(self.data_tab)
        scrollbar.pack(side="right", fill="y")
        
        self.display_text = tk.Text(self.data_tab, yscrollcommand=scrollbar.set, wrap="none",
                                  bg=self.current_theme['text_bg'], fg=self.current_theme['text_fg'],
                                  font=self.fonts["text"])
        self.display_text.pack(fill="both", expand=True)
        scrollbar.config(command=self.display_text.yview)
        
        # Quick View tab
        self.quick_view_tab = tk.Frame(self.notebook, bg=self.current_theme['frame_bg'])
        self.notebook.add(self.quick_view_tab, text=self.lang_dict[self.language]["quick_view"], state="hidden")
    
    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
        if file_path:
            try:
                self.data = pd.read_csv(file_path)
                self.file_path = file_path
                filename = file_path.split('/')[-1]
                self.file_label.config(text=filename)
                self.display_data(self.data.head())
                messagebox.showinfo(
                    self.lang_dict[self.language]["success"],
                    self.lang_dict[self.language]["file_loaded"]
                )
                self.notebook.tab(1, state="normal")
            except Exception as e:
                messagebox.showerror(
                    self.lang_dict[self.language]["error"],
                    self.lang_dict[self.language]["load_error"] + str(e)
                )
    
    def display_data(self, data):
        self.display_text.delete(1.0, tk.END)
        self.display_text.insert(tk.END, data.to_string())
    
    def remove_duplicates(self):
        if self.data is not None:
            old_size = len(self.data)
            self.data = self.data.drop_duplicates()
            new_size = len(self.data)
            self.display_data(self.data.head())
            messagebox.showinfo(
                self.lang_dict[self.language]["success"],
                f"{old_size - new_size}{self.lang_dict[self.language]['duplicates_removed']}"
            )
        else:
            messagebox.showwarning(
                self.lang_dict[self.language]["warning"],
                self.lang_dict[self.language]["no_data"]
            )
    
    def remove_null(self):
        if self.data is not None:
            old_size = len(self.data)
            self.data = self.data.dropna()
            new_size = len(self.data)
            self.display_data(self.data.head())
            messagebox.showinfo(
                self.lang_dict[self.language]["success"],
                f"{old_size - new_size}{self.lang_dict[self.language]['nulls_removed']}"
            )
        else:
            messagebox.showwarning(
                self.lang_dict[self.language]["warning"],
                self.lang_dict[self.language]["no_data"]
            )
    
    def fill_null(self):
        if self.data is not None:
            self.data = self.data.fillna(0).fillna("NULL")
            self.display_data(self.data.head())
            messagebox.showinfo(
                self.lang_dict[self.language]["success"],
                self.lang_dict[self.language]["nulls_filled"]
            )
        else:
            messagebox.showwarning(
                self.lang_dict[self.language]["warning"],
                self.lang_dict[self.language]["no_data"]
            )
    
    def show_stats(self):
        if self.data is not None:
            stats = self.data.describe(include='all')
            self.display_text.delete(1.0, tk.END)
            
            if self.language == "english":
                self.display_text.insert(tk.END, "Basic Statistics:\n\n")
            else:
                self.display_text.insert(tk.END, "الإحصائيات الأساسية:\n\n")
                
            self.display_text.insert(tk.END, stats.to_string())
            messagebox.showinfo(
                self.lang_dict[self.language]["success"],
                self.lang_dict[self.language]["stats_calculated"]
            )
        else:
            messagebox.showwarning(
                self.lang_dict[self.language]["warning"],
                self.lang_dict[self.language]["no_data"]
            )
    
    def show_info(self):
        if self.data is not None:
            lang = self.lang_dict[self.language]
            
            info = f"{lang['data_info']}:\n\n"
            info += f"{lang['rows']}{len(self.data)}\n"
            info += f"{lang['columns']}{len(self.data.columns)}\n\n"
            info += f"{lang['cols_list']}\n"
            for col in self.data.columns:
                info += f"- {col}\n"
            
            self.display_text.delete(1.0, tk.END)
            self.display_text.insert(tk.END, info)
            messagebox.showinfo(
                lang["success"],
                f"{lang['data_info']} {lang['success']}"
            )
        else:
            messagebox.showwarning(
                self.lang_dict[self.language]["warning"],
                self.lang_dict[self.language]["no_data"]
            )
    
    def show_quick_view(self):
        if self.data is not None:
            for widget in self.quick_view_tab.winfo_children():
                widget.destroy()
            
            canvas = tk.Canvas(self.quick_view_tab, bg=self.current_theme['frame_bg'])
            scrollbar = ttk.Scrollbar(self.quick_view_tab, orient="vertical", command=canvas.yview)
            scrollable_frame = ttk.Frame(canvas)
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
            numeric_cols = self.data.select_dtypes(include=['number']).columns
            
            if len(numeric_cols) > 0:
                for i, col in enumerate(numeric_cols):
                    frame = ttk.Frame(scrollable_frame, borderwidth=2, relief="groove", padding=10)
                    frame.grid(row=i, column=0, sticky="ew", padx=5, pady=5)
                    
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
                    
                    if self.dark_mode:
                        fig.patch.set_facecolor('#252525')
                        ax1.set_facecolor('#252525')
                        ax2.set_facecolor('#252525')
                        for ax in [ax1, ax2]:
                            ax.tick_params(colors='white')
                            ax.xaxis.label.set_color('white')
                            ax.yaxis.label.set_color('white')
                            ax.title.set_color('white')
                    
                    self.data[col].hist(ax=ax1)
                    ax1.set_title(f'Histogram of {col}')
                    ax1.set_ylabel('Frequency')
                    
                    self.data[col].plot(kind='box', ax=ax2)
                    ax2.set_title(f'Box Plot of {col}')
                    
                    plt.tight_layout()
                    
                    canvas_fig = FigureCanvasTkAgg(fig, master=frame)
                    canvas_fig.draw()
                    canvas_fig.get_tk_widget().pack(fill="both", expand=True)
                    
                    stats_frame = ttk.Frame(frame)
                    stats_frame.pack(fill="x")
                    
                    stats = self.data[col].describe()
                    for j, (stat, val) in enumerate(stats.items()):
                        tk.Label(stats_frame, text=f"{stat}: {val:.2f}", 
                               bg=self.current_theme['frame_bg'], fg=self.current_theme['fg'],
                               font=self.fonts["text"]).grid(row=0, column=j, padx=5)
            else:
                tk.Label(scrollable_frame, 
                       text=self.lang_dict[self.language]["no_data"],
                       bg=self.current_theme['frame_bg'], fg=self.current_theme['fg'],
                       font=self.fonts["text"]).pack()
            
            cat_cols = self.data.select_dtypes(include=['object']).columns
            if len(cat_cols) > 0:
                cat_frame = ttk.Frame(scrollable_frame, borderwidth=2, relief="groove", padding=10)
                cat_frame.grid(row=len(numeric_cols), column=0, sticky="ew", padx=5, pady=5)
                
                tk.Label(cat_frame, 
                       text=self.lang_dict[self.language]["cols_list"],
                       bg=self.current_theme['frame_bg'], fg=self.current_theme['fg'],
                       font=self.fonts["header"]).pack()
                
                for col in cat_cols:
                    col_frame = ttk.Frame(cat_frame)
                    col_frame.pack(fill="x", pady=5)
                    
                    tk.Label(col_frame, text=f"{col}:", 
                           bg=self.current_theme['frame_bg'], fg=self.current_theme['fg'],
                           font=self.fonts["text"]).pack(side="left")
                    
                    top_values = self.data[col].value_counts().head(5)
                    values_text = ", ".join([f"{val} ({count})" for val, count in top_values.items()])
                    tk.Label(col_frame, text=values_text, 
                           bg=self.current_theme['frame_bg'], fg=self.current_theme['fg'],
                           font=self.fonts["text"]).pack(side="left", padx=5)
            
            self.notebook.select(1)
            messagebox.showinfo(
                self.lang_dict[self.language]["success"],
                self.lang_dict[self.language]["quick_view_gen"]
            )
        else:
            messagebox.showwarning(
                self.lang_dict[self.language]["warning"],
                self.lang_dict[self.language]["no_data"]
            )
    
    def export_data(self):
        if self.data is not None:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
                title=self.lang_dict[self.language]["export"]
            )
            if file_path:
                try:
                    self.data.to_csv(file_path, index=False)
                    messagebox.showinfo(
                        self.lang_dict[self.language]["success"],
                        self.lang_dict[self.language]["data_exported"]
                    )
                except Exception as e:
                    messagebox.showerror(
                        self.lang_dict[self.language]["error"],
                        self.lang_dict[self.language]["export_error"] + str(e)
                    )
        else:
            messagebox.showwarning(
                self.lang_dict[self.language]["warning"],
                self.lang_dict[self.language]["no_data"]
            )
    
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        theme = "dark" if self.dark_mode else "light"
        self.current_theme = self.themes[theme]
        self.apply_theme()
        
        if hasattr(self, 'canvas_fig'):
            self.update_plot_theme()
    
    def apply_theme(self):
        theme = self.current_theme
        self.root.config(bg=theme['bg'])
        
        for widget in self.root.winfo_children():
            self.update_widget_theme(widget)
    
    def update_widget_theme(self, widget):
        theme = self.current_theme
        widget_type = widget.winfo_class()
        
        if widget_type in ('TFrame', 'Frame'):
            widget.config(bg=theme['frame_bg'])
        elif widget_type == 'Label':
            widget.config(bg=theme['bg'], fg=theme['fg'], font=self.fonts["text"])
        elif widget_type == 'Button':
            widget.config(bg=theme['button_bg'], fg=theme['button_fg'],
                         activebackground=theme['button_active'],
                         activeforeground=theme['button_fg'],
                         font=self.fonts["button"])
        elif widget_type == 'Text':
            widget.config(bg=theme['text_bg'], fg=theme['text_fg'],
                         insertbackground=theme['text_fg'],
                         font=self.fonts["text"])
        elif widget_type == 'LabelFrame':
            widget.config(bg=theme['bg'], fg=theme['fg'],
                         labelanchor='n', font=self.fonts["header"])
        
        for child in widget.winfo_children():
            self.update_widget_theme(child)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalyzerApp(root)
    root.mainloop()