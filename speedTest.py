import speedtest
#pip install speedtest-cli
import tkinter as tk

def check_internet_speed():
    st = speedtest.Speedtest()
    print("...Testing Speed...")
    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000

    st.get_best_server()
    ping = st.results.ping

    speed_test_results = {
        'download': round(download, 2),
        'upload': round(upload, 2),
        'ping': round(ping, 2)
    }
    return speed_test_results

def run_test():
    results = check_internet_speed()
    strvar_download.set(f"Download: {results['download']} Mbps")
    strvar_upload.set(f"Upload: {results['upload']} Mbps")
    strvar_ping.set(f"Ping: {results['ping']} ms")
    print("done testing")  

#main GUI window setup
window = tk.Tk()
window.geometry("250x150")
window.title('Speed Test')

#variables for results
strvar_download = tk.StringVar()
strvar_upload = tk.StringVar()
strvar_ping = tk.StringVar()
strvar_download.set("Download:")
strvar_upload.set("Upload:")
strvar_ping.set("Ping:")

#Button to execute speed test
btn_TestSpeed = tk.Button(window, text = 'Test Internet Speeds', width = 20, command = run_test)
btn_TestSpeed.pack()

#Labels For Results
txt_Download = tk.Label(window, textvariable = strvar_download)
txt_Download.pack() 
txt_upload = tk.Label(window, textvariable = strvar_upload)
txt_upload.pack()
txt_ping = tk.Label(window, textvariable = strvar_ping)
txt_ping.pack()  

#run program
window.mainloop()

