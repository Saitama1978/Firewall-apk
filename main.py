from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
import psutil

class FirewallApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        # Header Section - Kulay Blue para Professional ang dating
        header = BoxLayout(orientation='vertical', size_hint_y=0.2, padding=10)
        with header.canvas.before:
            Color(0.1, 0.4, 0.7, 1)  # Deep Blue background
            self.rect = Rectangle(size=header.size, pos=header.pos)
        header.bind(size=self._update_rect, pos=self._update_rect)

        header.add_widget(Label(
            text="FIREWALL MASTER",
            font_size='22sp',
            bold=True
        ))
        header.add_widget(Label(
            text="Developer: Renante Fullo",
            font_size='14sp'
        ))
        self.add_widget(header)

        # Scrollable Area para sa Listahan ng Apps
        self.scroll = ScrollView(size_hint_y=0.7)
        self.app_list = GridLayout(cols=1, spacing=10, size_hint_y=None, padding=10)
        self.app_list.bind(minimum_height=self.app_list.setter('height'))
        
        # Unang pag-load ng listahan
        self.refresh_list()
        
        self.scroll.add_widget(self.app_list)
        self.add_widget(self.scroll)

        # Bottom Button para sa Refresh
        self.refresh_btn = Button(
            text="REFRESH RUNNING APPS",
            size_hint_y=0.1,
            background_color=(0, 0.7, 0.3, 1), # Green button
            bold=True
        )
        self.refresh_btn.bind(on_press=self.refresh_list)
        self.add_widget(self.refresh_btn)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def refresh_list(self, *args):
        self.app_list.clear_widgets()
        
        # Gamit ang psutil para isa-isahin ang mga tumatakbong app
        # Kukuha tayo ng pid, name, at cmdline para sa mas malinaw na pangalan
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                # Isang box para sa bawat entry
                row = BoxLayout(size_hint_y=None, height=70, padding=5)
                
                # Mas detalyadong pagkuha ng pangalan
                p_info = proc.info
                display_name = p_info['name']
                
                # Kung may cmdline (karaniwan nandoon ang package name tulad ng com.android.chrome)
                if p_info['cmdline'] and len(p_info['cmdline']) > 0:
                    # Kinukuha ang huling part ng command path
                    display_name = p_info['cmdline'][0].split('/')[-1]

                # Label para sa App Info
                app_label = Label(
                    text=f"App: {display_name}\nPID: {p_info['pid']}",
                    halign='left',
                    valign='middle',
                    size_hint_x=0.7,
                    font_size='14sp'
                )
                app_label.bind(size=app_label.setter('text_size'))

                # STOP Button para i-kill ang process
                stop_btn = Button(
                    text="STOP",
                    size_hint_x=0.3,
                    background_color=(0.9, 0.1, 0.1, 1) # Red button
                )
                # I-bind ang function para itigil ang PID na napili
                stop_btn.bind(on_press=lambda btn, p=p_info['pid']: self.stop_process(p))
                
                row.add_widget(app_label)
                row.add_widget(stop_btn)
                self.app_list.add_widget(row)

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Laktawan ang mga apps na bawal pakialaman ng system
                continue

    def stop_process(self, pid):
        try:
            p = psutil.Process(pid)
            p.terminate() # Utos na itigil ang app
            self.refresh_list() # I-refresh ang listahan matapos i-stop
        except Exception as e:
            print(f"Hindi ma-stop ang app: {e}")

class MainApp(App):
    def build(self):
        return FirewallApp()

if __name__ == "__main__":
    MainApp().run()