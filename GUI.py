import customtkinter
import tkinter as tk
import json
import os
import sys
import time
import subprocess
from playsound import playsound
from tkinter import ttk
from tkinter import filedialog
import requests
import fade
from PIL import Image



ico_path = os.path.join(os.path.dirname(__file__), "icon.ico")
json_path = os.path.join(os.path.dirname(__file__), "Blue.json")
json2_path = os.path.join(os.path.dirname(__file__), "settings.json")
ahk_path = os.path.join(os.path.dirname(__file__), "MekoAssist.ahk")
audio_path = os.path.join(os.path.dirname(__file__), "audio.mp3")

script_dir = os.path.dirname(os.path.abspath(__file__))
PASTEBIN_URL = "-------"
tomphy = fade.water("""
                     
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄         ▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ 
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌     ▐░▌     
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌     ▐░▌     
     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌     ▐░▌     
      ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀            ▀         ▀       ▀      
                                                                              
""") * 10

Gui_path = os.path.join(script_dir, "gui.py")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme(json_path)

class AuthWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.wm_iconbitmap(ico_path)
        self.title("login")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.titlelabel = customtkinter.CTkLabel(self, text="Enter Credentials")
        self.titlelabel.grid(row=0, column=0, columnspan=3, pady=20, padx=10, sticky="ew")

        self.usernamelabel = customtkinter.CTkLabel(self, text="Username:")
        self.usernamelabel.grid(row=1, column=0, pady=10, padx=0, sticky="e")

        self.usernameentry = customtkinter.CTkEntry(self)
        self.usernameentry.grid(row=1, column=1, pady=10, padx=10, columnspan=2, sticky="ew")
        
        self.passwordlabel = customtkinter.CTkLabel(self, text="Password:")
        self.passwordlabel.grid(row=2, column=0, pady=10, padx=0, sticky="e")

        self.passwordentry = customtkinter.CTkEntry(self, show="*")
        self.passwordentry.grid(row=2, column=1, pady=10, padx=10, columnspan=2, sticky="ew")
        
        self.login_button = customtkinter.CTkButton(self, text="Login", command=self.validate_credentials)
        self.login_button.grid(row=3, column=1, pady=10, padx=10, columnspan=2, sticky="ew")

    def validate_credentials(self):
        username = self.usernameentry.get()
        password = self.passwordentry.get()
        
     
        response = requests.get(PASTEBIN_URL)
        if response.status_code == 200:
            credentials = response.text.splitlines()
            for credential in credentials:
                stored_username, stored_password = credential.split(',')
                if username == stored_username and password == stored_password:
                    self.destroy()  
                    runGUI()  
                    return
            customtkinter.CTkLabel(self, text="Invalid credentials", fg_color="red").grid(row=4, column=0, columnspan=3, sticky="ew")
        else:
            customtkinter.CTkLabel(self, text="Error fetching credentials", fg_color="red").grid(row=4, column=0, columnspan=3, sticky="ew")
        



def runGUI():
    app = App()
    App.mainloop(self= app)    
    

class ConfigWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Insert your config")
        
        self.parent = parent
        
        self.iconbitmap(ico_path)
        
       
        style = ttk.Style(self)
        style.theme_use("clam")

        
        self.configure(bg="#202020")  
        style.configure(".", background="#202020", foreground="#FFFFFF", fieldbackground="#303030")  

       
        self.text_entry = tk.Text(self, width=50, height=10, bg="#303030", fg="#FFFFFF")
        self.text_entry.pack(pady=10)

       
        choose_button = ttk.Button(self, text="Choose Config", command=self.choose_file, style="DarkButton.TButton")
        choose_button.pack(pady=5)

       
        insert_button = ttk.Button(self, text="Insert Config", command=self.insert_text, style="DarkButton.TButton")
        insert_button.pack(pady=5)

        
        style.configure("DarkButton.TButton", background="#404040", foreground="#FFFFFF", bordercolor="#303030")
    
    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as f:
                text = f.read()
                self.text_entry.delete('1.0', tk.END)  
                self.text_entry.insert(tk.END, text)

    def insert_text(self):
        text = self.text_entry.get('1.0', tk.END)
        save_to_json(text)
        self.destroy()  

def save_to_json(text):
    with open(json2_path, "w") as f:
        f.write(text)
    print("\033[31mupdated settings\033[0m")
    


class KeybindChanger(customtkinter.CTk):
    def __init__(self, keybind_label):
        super().__init__()
    

        self.wm_iconbitmap(ico_path)
   
        self.keybind_label = keybind_label
  
       
        self.title("Change Keybind")
        self.geometry("300x150")
        
        
        
      
        self.label = customtkinter.CTkLabel(self, text="Press a key or mouse button to choose the keybind")
        self.label.pack(pady=10)

        
        self.bind("<KeyPress>", self.on_key_press)
        self.bind("<Button>", self.on_mouse_press)

    def on_key_press(self, event):
        key = event.keysym
        if len(key) == 1 and 'a' <= key <= 'z':
            key = key.upper()
        self.update_keybind(key)

    def on_mouse_press(self, event):
        mouse_button = event.num
        if mouse_button == 4:
            new_keybind = "XButton1"
        elif mouse_button == 5:
            new_keybind = "XButton2"
        elif mouse_button == 3:
            new_keybind = "RButton"
        else:
            new_keybind = f"Mouse{mouse_button}"
        self.update_keybind(new_keybind)

    def update_keybind(self, new_keybind):
        json_file = json2_path
        with open(json_file, 'r') as f:
            data = json.load(f)

        data["MekoAssist"]["Binds"]["Keybind"] = new_keybind

        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)
        
        self.label.configure(text=f"Keybind changed to: {new_keybind}")
        self.keybind_label.configure(text=f"Selected Keybind: {new_keybind}")
         

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        print(tomphy)
        print(tomphy)
        print(tomphy)
        print(tomphy)
        print(tomphy)
        print(tomphy)
        print(tomphy)
        print(tomphy)
        print(tomphy)
        print(tomphy)
        print(tomphy)
        print(tomphy)
        print(tomphy)
        print(tomphy)
        print(tomphy)
        print(tomphy)
        print(tomphy)
        print(tomphy)
        
        self.wm_iconbitmap(ico_path)

        
        self.title("✎TPHy (made by @lonelyintrovertedboy)")
        self.geometry(f"{770}x{720}")

        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
    
        
    
        
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=0, padx=(0, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Assist")
        self.tabview.add("Misc")
        self.tabview.add("Visuals")
        
        
        self.tab1_frame = customtkinter.CTkFrame(self.tabview.tab("Assist"), fg_color="transparent")
        self.tabview.tab("Assist").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Assist").grid_rowconfigure(0, weight=0)  
        self.tabview.tab("Assist").grid_rowconfigure(1, weight=0)  
        self.tab1_frame.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        
        
        self.tab2_frame = customtkinter.CTkFrame(self.tabview.tab("Misc"), fg_color="transparent")
        self.tabview.tab("Misc").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Misc").grid_rowconfigure(0, weight=0)  
        self.tabview.tab("Misc").grid_rowconfigure(1, weight=0)  
        self.tab2_frame.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        self.tab3_frame = customtkinter.CTkFrame(self.tabview.tab("Visuals"), fg_color="transparent")
        self.tabview.tab("Visuals").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Visuals").grid_rowconfigure(0, weight=0)  
        self.tabview.tab("Visuals").grid_rowconfigure(1, weight=0)  
        self.tab3_frame.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        
    
        
        
        
        
        
        self.slider_title_label = customtkinter.CTkLabel(self.tab1_frame, text="Smoothness X")
        self.slider_title_label.grid(row=0, column=0, padx=(20, 0), pady=(10, 0), sticky="w")
        
        initial_smoothness_x = self.load_smoothness_x_from_json()
        
        initial_smoothness_y = self.load_smoothness_y_from_json()
        
        initial_prediction_x = self.load_prediction_x_from_json()
        
        initial_sat = self.load_color_from_json()
        
        initial_linearcurve_x = self.load_bezier_from_json()
        
        initial_linearcurve_y = self.load_bezier2_from_json()
        
        initial_fovoffset_x = self.load_fovoffset_x_from_json()
        
        initial_fovoffset_y = self.load_fovoffset_y_from_json()
        
      
        self.slider_1 = customtkinter.CTkSlider(self.tab1_frame, from_=0, to=100, number_of_steps=100)
        self.slider_1.set(initial_smoothness_x)
        self.slider_1.grid(row=1, column=0, padx=(20, 10), pady=(0, 10), sticky="ew")

      
        self.slider_value_label = customtkinter.CTkLabel(self.tab1_frame, text =f"Value: {initial_smoothness_x}")
        self.slider_value_label.grid(row=2, column=0, padx=(20, 0), pady=(10, 0), sticky="w")

     
        self.slider_1.bind("<ButtonRelease-1>", self.update_smoothness_x)
        self.slider_1.bind("<B1-Motion>", self.update_smoothness_x)
        
   
        self.slider_2 = customtkinter.CTkSlider(self.tab1_frame, from_=0, to=100, number_of_steps=100)
        self.slider_2.set(initial_smoothness_y)
        self.slider_2.grid(row=4, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

    
        self.slider_value_label_2 = customtkinter.CTkLabel(self.tab1_frame, text=f"Value: {initial_smoothness_y}")
        self.slider_value_label_2.grid(row=5, column=0, padx=(20, 0), pady=(15, 0), sticky="w")

    
        self.slider_2.bind("<ButtonRelease-1>", self.update_smoothness_y)
        self.slider_2.bind("<B1-Motion>", self.update_smoothness_y)
        
        self.slider_title_label2 = customtkinter.CTkLabel(self.tab1_frame, text="Smoothness Y")
        self.slider_title_label2.grid(row=3, column=0, padx=(20, 0), pady=(10, 10), sticky="w")
        
        self.checkboxlabel =customtkinter.CTkLabel(self.tab1_frame, text="Prediction")
        self.checkboxlabel.grid(row=6, column=0, padx=(20, 0), pady=(10, 10), sticky="w")
        
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.tab1_frame, command=self.toggle_prediction)
        self.checkbox_1.grid(row=7, column=0, pady=(10, 0), padx=(20,115), sticky="n")

        initial_prediction_state = self.load_prediction_state_from_json()
        self.checkbox_1.select() if initial_prediction_state else self.checkbox_1.deselect()
        self.checkbox_1.configure(text="True" if initial_prediction_state else "False")        

                   
       
        initial_prediction_mode = self.load_prediction_mode_from_json
        
        self.prediction_mode_var = tk.StringVar(self)
        self.prediction_mode_var.set(self.load_prediction_mode_from_json())  # Set default mode
        self.prediction_options = ["Multiplication", "Ideal",]
        self.prediction_optionmenu = customtkinter.CTkOptionMenu(self.tab1_frame, values=self.prediction_options,
                                                                 variable=self.prediction_mode_var,
                                                                 dropdown_hover_color="blue",
                                                                 width=200)
        self.prediction_optionmenu.grid(row=8, column=0, pady=(25, 15))

   
        self.prediction_optionmenu.bind("<ButtonRelease-1>", self.update_prediction_mode)
        self.prediction_optionmenu.bind("<<ComboboxSelected>>", self.update_prediction_mode)
        
  
        self.slider_title_label = customtkinter.CTkLabel(self.tab1_frame, text="Prediction X")
        self.slider_title_label.grid(row=9, column=0, padx=(20, 0), pady=(10, 10), sticky="w") 

     
        self.slider_3 = customtkinter.CTkSlider(self.tab1_frame, from_=1, to=10, number_of_steps=9)
        self.slider_3.set(initial_prediction_x)
        self.slider_3.grid(row=10, column=0, padx=(20, 10), pady=(10, 15), sticky="ew")

  
        self.slider_value_label_3 = customtkinter.CTkLabel(self.tab1_frame, text=f"Value: {initial_prediction_x}")
        self.slider_value_label_3.grid(row=11, column=0, padx=(20, 0), pady=(10, 0), sticky="w")

        self.slider_3.bind("<ButtonRelease-1>", self.update_prediction_x)
        self.slider_3.bind("<B1-Motion>", self.update_prediction_x)
        
    
        self.keybind_frame = customtkinter.CTkFrame(self.tab1_frame)
        self.keybind_frame.grid(row=0, column=1, padx=(20, 0), pady=(0, 0), sticky="w")

  
        self.slider_title_label = customtkinter.CTkLabel(self.keybind_frame, text="Keybinds")
        self.slider_title_label.pack()

 
        self.button = customtkinter.CTkButton(self.keybind_frame, text="Change Keybind", command=self.open_keybind_changer)
        self.button.pack(pady=10)

  
        self.selected_keybind_label = customtkinter.CTkLabel(self.tab1_frame, text="Select Keybind: None")
        self.selected_keybind_label.grid(row=1, column=1, padx=(20, 0), pady=(10, 0), sticky="w")

 
        initial_keybind = self.load_initial_keybind()
        if initial_keybind:
            self.selected_keybind_label.configure(text=f"Keybind: {initial_keybind}")
            
        self.color = customtkinter.CTkLabel(self.tab1_frame, text="Sensitivity")
        self.color.grid(row=2, column=1, padx=(20, 0), pady=(10, 0), sticky="w")
            
        self.slider_4 = customtkinter.CTkSlider(self.tab1_frame, from_=1, to=100, number_of_steps=100)
        self.slider_4.set(initial_sat)
        self.slider_4.grid(row=3, column=1, padx=(20, 10), pady=(10, 15), sticky="ew")
            
        self.slider_value_label_4 = customtkinter.CTkLabel(self.tab1_frame, text=f"Value: {initial_sat}")
        self.slider_value_label_4.grid(row=4, column=1, padx=(20, 0), pady=(10, 0), sticky="w")    
        
        self.slider_4.bind("<ButtonRelease-1>", self.update_color)
        self.slider_4.bind("<B1-Motion>", self.update_color)
        
        self.bezier = customtkinter.CTkLabel(self.tab1_frame, text="Bezier")
        self.bezier.grid(row=5, column=1, padx=(20, 0), pady=(0, 0), sticky="w")
        
        self.linearX = customtkinter.CTkLabel(self.tab1_frame, text="Linear Curve X")
        self.linearX.grid(row=6, column=1, padx=(20, 0), pady=(0, 0), sticky="w")

        self.slider_5 = customtkinter.CTkSlider(self.tab1_frame, from_=0.1, to=1, number_of_steps=10000)
        self.slider_5.set(initial_linearcurve_x) 
        self.slider_5.grid(row=7, column=1, padx=(20, 10), pady=(0, 0), sticky="ew")

        self.slider_value_label_5 = customtkinter.CTkLabel(self.tab1_frame, text=f"Value: {initial_linearcurve_x}")
        self.slider_value_label_5.grid(row=8, column=1, padx=(20, 0), pady=(0, 0), sticky="w")    

        self.slider_5.bind("<ButtonRelease-1>", self.update_linearcurve_x)
        self.slider_5.bind("<B1-Motion>", self.update_linearcurve_x)

        
        
        self.linearY = customtkinter.CTkLabel(self.tab1_frame, text="Linear Curve Y")
        self.linearY.grid(row=9, column=1, padx=(20, 0), pady=(0, 0), sticky="w")

        self.slider_6 = customtkinter.CTkSlider(self.tab1_frame, from_=0.1, to=1, number_of_steps=10000)
        self.slider_6.set(initial_linearcurve_y)  
        self.slider_6.grid(row=10, column=1, padx=(20, 10), pady=(0, 0), sticky="ew")

        self.slider_value_label_6 = customtkinter.CTkLabel(self.tab1_frame, text=f"Value: {initial_linearcurve_y}")
        self.slider_value_label_6.grid(row=11, column=1, padx=(20, 0), pady=(0, 0), sticky="w")    

        self.slider_6.bind("<ButtonRelease-1>", self.update_linearcurve_y)
        self.slider_6.bind("<B1-Motion>", self.update_linearcurve_y)


        self.fov_label = customtkinter.CTkLabel(self.tab1_frame, text="Enter your in-game FOV (70-120):")
        self.fov_label.grid(row=0, column=2, padx=(20,0), pady=(10,0), sticky="w")
        
        self.fov_entry = customtkinter.CTkEntry(self.tab1_frame, validate="key")
        self.fov_entry['validatecommand'] = (self.register(self.validate_fov), '%P')
        self.fov_entry.grid(row=1, column=2, padx=(20,10), pady=(10,0), sticky="w")
        
     
        self.update_fov_button = customtkinter.CTkButton(self.tab1_frame, text="Update FOV", command=self.update_camera_fov)
        self.update_fov_button.grid(row=2, column=2, padx=(20, 0), pady=(10, 0), sticky="w")    
        
        self.fov_label_2 = customtkinter.CTkLabel(self.tab1_frame, text="FOV circle (not visual)")
        self.fov_label_2.grid(row=3, column=2, padx=(20,10), pady=(10,0), sticky="w")
        
        self.FovX = customtkinter.CTkLabel(self.tab1_frame, text="FOV Offset X")
        self.FovX.grid(row=4, column=2, padx=(20, 0), pady=(10, 0), sticky="w")
        
        self.slider_8 = customtkinter.CTkSlider(self.tab1_frame, from_=1, to=10, number_of_steps=100)
        self.slider_8.set(initial_fovoffset_x)  
        self.slider_8.grid(row=5, column=2, padx=(20, 10), pady=(0, 0), sticky="ew")

        self.slider_value_label_8 = customtkinter.CTkLabel(self.tab1_frame, text=f"Value: {initial_fovoffset_x}")
        self.slider_value_label_8.grid(row=6, column=2, padx=(20, 0), pady=(0, 0), sticky="w")    

        self.slider_8.bind("<ButtonRelease-1>", self.update_fovoffset_x)
        self.slider_8.bind("<B1-Motion>", self.update_fovoffset_x)
        
        self.FovY = customtkinter.CTkLabel(self.tab1_frame, text="FOV Offset Y")
        self.FovY.grid(row=7, column=2, padx=(20, 0), pady=(10, 0), sticky="w")
        
        self.slider_9 = customtkinter.CTkSlider(self.tab1_frame, from_=0, to=10, number_of_steps=100)
        self.slider_9.set(initial_fovoffset_y)  
        self.slider_9.grid(row=8, column=2, padx=(20, 10), pady=(0, 0), sticky="ew")

        self.slider_value_label_9 = customtkinter.CTkLabel(self.tab1_frame, text=f"Value: {initial_fovoffset_y}")
        self.slider_value_label_9.grid(row=9, column=2, padx=(20, 0), pady=(0, 0), sticky="w")    

        self.slider_9.bind("<ButtonRelease-1>", self.update_fovoffset_y)
        self.slider_9.bind("<B1-Motion>", self.update_fovoffset_y)
        
        self.inject = customtkinter.CTkButton(self.tab1_frame, text="apply", command=self.run_ahk_script)
        self.inject.grid(row=10, column=2, padx=(20, 0), pady=(0, 0), sticky="w")
        
#---------------------------------------TAB2----------------------------------------------------------------------------------------------------------

        self.whatthesigma = customtkinter.CTkButton(self.tab2_frame, text="silent aim very real")
        self.whatthesigma.grid(row=0, column=0, padx=(20, 10), pady=(0, 10), sticky="ew")
        self.whatthesigma.bind("<Button-1>", self.play_audio)
        
        self.config = customtkinter.CTkButton(self.tab2_frame, text="import config", command=self.open_config_changer)
        self.config.grid(row=1, column=0, padx=(20, 10), pady=(0, 10), sticky="ew")
        
        refresh_button = customtkinter.CTkButton(self, text="Refresh Script", command=self.refresh_script)
        refresh_button.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        

        
#---------------------------------------DEFINE SECTION--------------------------------------------------------------------------------------------------

    def load_initial_keybind(self):
        try:
            with open(json2_path, "r") as f:
                data = json.load(f)
                return data.get("MekoAssist", {}).get("Binds", {}).get("Keybind", "None")
        except FileNotFoundError:
            print("settings.json file not found.")
            return "None"
        except Exception as e:
            print(f"An error occurred while loading the initial keybind: {e}")
            return "None"
    
    def validate_fov(self, new_value):
        if new_value.isdigit():
            fov = int(new_value)
            return 70 <= fov <= 120
        elif new_value == "":
            return True
        else:
            return False

    def update_camera_fov(self):
        new_fov = int(self.fov_entry.get())
        with open(json2_path, "r") as f:
            data = json.load(f)

        data["MekoAssist"]["Misc"]["CameraToGunFOV"] = new_fov

        with open(json2_path, "w") as f:
            json.dump(data, f, indent=4)
        
        print("CameraToGunFOV updated successfully!")

    def load_smoothness_x_from_json(self):
        try:
            with open(json2_path, "r") as f:
                data = json.load(f)
            return data.get("MekoAssist", {}).get("Easing", {}).get("SmoothnessX", 0)
        except FileNotFoundError:
            print("settings.json file not found.")
            return 0
        except Exception as e:
            print(f"An error occurred while loading Smoothness X from JSON: {e}")
            return 0    
        
    def load_color_from_json(self):
            try:
                with open(json2_path, "r") as f:
                    data = json.load(f)
                return data.get("MekoAssist", {}).get("Color", {}).get("Saturation", 0)
            except FileNotFoundError:
                print("settings.json file not found.")
                return 0
            except Exception as e:
                print(f"An error occurred while loading Smoothness X from JSON: {e}")
                return 0    
            
    def load_bezier_from_json(self):
                try:
                    with open(json2_path, "r") as f:
                        data = json.load(f)
                    return data.get("MekoAssist", {}).get("Bezier", {}).get("LinearCurveX", 0)
                except FileNotFoundError:
                    print("settings.json file not found.")
                    return 0
                except Exception as e:
                    print(f"An error occurred while loading LinearCurveX from JSON: {e}")
                    return 0    
                
    def load_bezier2_from_json(self):
                try:
                    with open(json2_path, "r") as f:
                        data = json.load(f)
                    return data.get("MekoAssist", {}).get("Bezier", {}).get("LinearCurveY", 0)
                except FileNotFoundError:
                    print("settings.json file not found.")
                    return 0
                except Exception as e:
                    print(f"An error occurred while loading LinearCurveY from JSON: {e}")
                    return 0  
        
    def load_smoothness_y_from_json(self):
        try:
            with open(json2_path, "r") as f:
                data = json.load(f)
            return data.get("MekoAssist", {}).get("Easing", {}).get("SmoothnessY", 0)
        except FileNotFoundError:
            print("settings.json file not found.")
            return 0
        except Exception as e:
            print(f"An error occurred while loading Smoothness Y from JSON: {e}")
            return 0  
        
    def load_fovoffset_x_from_json(self):
        try:
            with open(json2_path, "r") as f:
                data = json.load(f)
            return data.get("MekoAssist", {}).get("FOV", {}).get("FOVOffsetX", 0)
        except FileNotFoundError:
            print("settings.json file not found.")
            return 0
        except Exception as e:
            print(f"An error occurred while loading FOVOffsetX from JSON: {e}")
            return 0          
        
    def load_fovoffset_y_from_json(self):
        try:
            with open(json2_path, "r") as f:
                data = json.load(f)
            return data.get("MekoAssist", {}).get("FOV", {}).get("FOVOffsetY", 0)
        except FileNotFoundError:
            print("settings.json file not found.")
            return 0
        except Exception as e:
            print(f"An error occurred while loading FOVOffsetY from JSON: {e}")
            return 0          
        
    def load_prediction_x_from_json(self):
        try:
            with open(json2_path, "r") as f:
                data = json.load(f)
            return data.get("MekoAssist", {}).get("Easing", {}).get("Prediction", {}).get("PredictionX", 0)
        except FileNotFoundError:
            print("settings.json file not found.")
            return 0
        except Exception as e:
            print(f"An error occurred while loading Prediction X from JSON: {e}")
            return 0

    def open_keybind_changer(self):
        keybind_changer = KeybindChanger(self.selected_keybind_label)
        keybind_changer.mainloop()
        
    def open_config_changer(self):
        config_changer = ConfigWindow(self.config)  
        config_changer.mainloop()      
        
    

   
    def update_prediction_mode(self, event=None):
        selected_mode = self.prediction_mode_var.get()
        try:
            with open(json2_path, "r") as f:
                data = json.load(f)

         
            data["MekoAssist"]["Easing"]["Prediction"]["Mode"] = selected_mode

         
            with open(json2_path, "w") as f:
                json.dump(data, f, indent=4)

            

        except FileNotFoundError:
            print("settings.json file not found.")
        except Exception as e:
            print(f"An error occurred while updating prediction mode: {e}") 
        self.prediction_optionmenu.bind("<<ComboboxSelected>>", self.update_prediction_mode)   
    

            
    def update_slider_value_3(self, event):
        current_value = self.slider_3.get()
        self.slider_value_label_3.configure(text=f"Value: {int(current_value)}")    

    def update_slider_value(self, event):
        current_value = self.slider_1.get()
        self.slider_value_label.configure(text=f"Value: {int(current_value)}")

    def update_slider_value_2(self, event):
        current_value = self.slider_2.get()
        self.slider_value_label_2.configure(text=f"Value: {int(current_value)}")
        
    def update_slider_value_4(self, event):
        current_value = self.slider_4.get()
        self.slider_value_label_4.configure(text=f"Value: {int(current_value)}")
        
    def update_slider_value_5(self, event):
        current_value = self.slider_5.get()
        self.slider_value_label_5.configure(text=f"Value: {current_value:.3f}")  
            
    def update_slider_value_8(self, event):
        current_value = self.slider_8.get()
        self.slider_value_label_8.configure(text=f"Value: {current_value:.1f}")  
        
    def update_slider_value_9(self, event):
        current_value = self.slider_9.get()
        self.slider_value_label_9.configure(text=f"Value: {current_value:.1f}")  
        
    def update_slider_value_6(self, event):
        current_value = self.slider_6.get()
        self.slider_value_label_6.configure(text=f"Value: {current_value:.3f}")  
        
    def update_smoothness_x(self, event):
        current_value = self.slider_1.get()
        self.slider_value_label.configure(text=f"Value: {int(current_value)}")

        try:
            with open(json2_path, "r") as f:
                data = json.load(f)

        
            data["MekoAssist"]["Easing"]["SmoothnessX"] = int(current_value)

       
            with open(json2_path, "w") as f:
                json.dump(data, f, indent=4)


        except FileNotFoundError:
            print("settings.json file not found.")
        except Exception as e:
            print(f"An error occurred while updating Smoothness X: {e}")
            
    def update_fovoffset_x(self, event):
        current_value = self.slider_8.get()
        rounded_value = round(current_value, 3) 
        self.slider_value_label_8.configure(text=f"Value: {rounded_value:.1f}")

        try:
            with open(json2_path, "r") as f:
                data = json.load(f)

          
            data["MekoAssist"]["FOV"]["FOVOffsetX"] = rounded_value

          
            with open(json2_path, "w") as f:
                json.dump(data, f, indent=4)
        except FileNotFoundError:
            print("settings.json file not found.")
        except Exception as e:
            print(f"An error occurred while updating FOVOffsetX: {e}")
            
    def update_fovoffset_y(self, event):
        current_value = self.slider_9.get()
        rounded_value = round(current_value, 3) 
        self.slider_value_label_9.configure(text=f"Value: {rounded_value:.1f}")

        try:
            with open(json2_path, "r") as f:
                data = json.load(f)

        
            data["MekoAssist"]["FOV"]["FOVOffsetY"] = rounded_value

        
            with open(json2_path, "w") as f:
                json.dump(data, f, indent=4)
        except FileNotFoundError:
            print("settings.json file not found.")
        except Exception as e:
            print(f"An error occurred while updating FOVOffsetY: {e}")
            
    def update_linearcurve_x(self, event):
        current_value = self.slider_5.get()
        rounded_value = round(current_value, 3)  
        self.slider_value_label_5.configure(text=f"Value: {rounded_value:.3f}")

        try:
            with open(json2_path, "r") as f:
                data = json.load(f)

    
            data["MekoAssist"]["Bezier"]["LinearCurveX"] = rounded_value

     
            with open(json2_path, "w") as f:
                json.dump(data, f, indent=4)
        except FileNotFoundError:
            print("settings.json file not found.")
        except Exception as e:
            print(f"An error occurred while updating LinearCurveX: {e}")
                
    def update_linearcurve_y(self, event):
        current_value = self.slider_6.get()
        rounded_value = round(current_value, 3) 
        self.slider_value_label_6.configure(text=f"Value: {rounded_value:.3f}")

        try:
            with open(json2_path, "r") as f:
                data = json.load(f)

     
            data["MekoAssist"]["Bezier"]["LinearCurveY"] = rounded_value

    
            with open(json2_path, "w") as f:
                json.dump(data, f, indent=4)
        except FileNotFoundError:
            print("settings.json file not found.")
        except Exception as e:
            print(f"An error occurred while updating LinearCurveY: {e}")
            
    def update_smoothness_y(self, event):
        current_value = self.slider_2.get()
        self.slider_value_label_2.configure(text=f"Value: {int(current_value)}")

        try:
            with open(json2_path, "r") as f:
                data = json.load(f)


            data["MekoAssist"]["Easing"]["SmoothnessY"] = int(current_value)

   
            with open(json2_path, "w") as f:
                json.dump(data, f, indent=4)
        except FileNotFoundError:
            print("settings.json file not found.")
        except Exception as e:
            print(f"An error occurred while updating Smoothness Y: {e}")  
            
    def update_color(self, event):
        current_value = self.slider_4.get()
        self.slider_value_label_4.configure(text=f"Value: {int(current_value)}")

        try:
            with open(json2_path, "r") as f:
                data = json.load(f)


            data["MekoAssist"]["Color"]["Saturation"] = int(current_value)

    
            with open(json2_path, "w") as f:
                json.dump(data, f, indent=4)
        except FileNotFoundError:
            print("settings.json file not found.")
        except Exception as e:
            print(f"An error occurred while updating Smoothness Y: {e}") 
          
    def update_prediction_x(self, event):
        current_value = self.slider_3.get()
        self.slider_value_label_3.configure(text=f"Value: {int(current_value)}")

        try:
            with open(json2_path, "r") as f:
                data = json.load(f)

      
            data["MekoAssist"]["Easing"]["Prediction"]["PredictionX"] = int(current_value)

      
            with open(json2_path, "w") as f:
                json.dump(data, f, indent=4)

        except FileNotFoundError:
            print("settings.json file not found.")
        except Exception as e:
            print(f"An error occurred while updating Prediction X: {e}")     
   
    def load_prediction_state_from_json(self):
        try:
            with open(json2_path, "r") as f:
                data = json.load(f)
            return data.get("MekoAssist", {}).get("Easing", {}).get("Prediction", {}).get("Enabled", False) == 1
        except FileNotFoundError:
            print("settings.json file not found.")
            return False
        except Exception as e:
            print(f"An error occurred while loading Prediction state from JSON: {e}")
            return False
    
    def toggle_prediction(self):
        try:
            with open(json2_path, "r") as f:
                data = json.load(f)

            
            new_state = not data["MekoAssist"]["Easing"]["Prediction"]["Enabled"]  
            data["MekoAssist"]["Easing"]["Prediction"]["Enabled"] = new_state

         
            with open(json2_path, "w") as f:
                json.dump(data, f, indent=4)

            
            self.checkbox_1.configure(text=str(new_state))

            

        except FileNotFoundError:
            print("settings.json file not found.")
        except Exception as e:
            print(f"An error occurred while updating Prediction setting: {e}")
            
    def load_prediction_mode_from_json(self):
            try:
                with open(json2_path, "r") as f:
                    data = json.load(f)
                return data.get("MekoAssist", {}).get("Easing", {}).get("Prediction", {}).get("Mode")
            except FileNotFoundError:
                print("settings.json file not found.")
                return None
            except Exception as e:
                print(f"An error occurred while loading prediction mode from JSON: {e}")
            return None
        
    def update_prediction_mode(self, event=None):
        selected_mode = self.prediction_mode_var.get()
        try:
            with open(json2_path, "r+") as f:
                data = json.load(f)

 
                data.setdefault("MekoAssist", {}).setdefault("Easing", {}).setdefault("Prediction", {})
                data["MekoAssist"]["Easing"]["Prediction"]["Mode"] = selected_mode

        
                f.seek(0)  
                json.dump(data, f, indent=4)
                f.truncate()

           

        except FileNotFoundError:
            print("settings.json file not found.")
        except Exception as e:
            print(f"An error occurred while updating prediction mode: {e}")
            
    def run_ahk_script(self, *args):
        subprocess.Popen([ahk_path], shell=True)       
        print("\033[31mAHK UPDATED\033[0m") 
            
#-----------------------------------------------TAB2------------------------------------------------------------------------

    def play_audio(self, event):
    
        audio_file = audio_path
        playsound(audio_file)
        
    def refresh_script(self):
        self.destroy()
        runGUI()

           
                 
if __name__ == "__main__":
    auth_app = AuthWindow()
    auth_app.mainloop()
