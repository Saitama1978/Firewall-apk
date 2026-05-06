from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

# Safe import para hindi mag-error ang APK
try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

class RAMSaverApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        layout.add_widget(Label(text="RAMSaver Pro", font_size='25sp', bold=True))
        layout.add_widget(Label(text="Developer: Renante Fullo", font_size='14sp'))
        
        self.label = Label(text="Initializing...")
        layout.add_widget(self.label)
        
        Clock.schedule_interval(self.update_info, 1)
        return layout

    def update_info(self, dt):
        if HAS_PSUTIL:
            mem = psutil.virtual_memory()
            self.label.text = f"RAM Usage: {mem.percent}%"
        else:
            self.label.text = "Running in Lite Mode (psutil not found)"

if __name__ == "__main__":
    RAMSaverApp().run()