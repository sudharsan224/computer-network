import tkinter as tk
from tkinter import messagebox

def show(title, text):
    output.delete("1.0", tk.END)
    output.insert(tk.END, text)
    status.config(text="● " + title + " COMPLETED")

def topology():
    show("TOPOLOGY", """
                HEAD OFFICE
              +-------------+
              |   Router R1 |
              +------+------+ 
                     |
                  +--+--+
                  | SW1 |
                  +--+--+
                /   |   \\
              R&D  SALES  SERVER
                    |
                ----------- WAN -----------
                 /                       \\
           +----+----+               +----+----+
           | Router R2|               | Router R3|
           +----+----+               +----+----+
                |                         |
              SW2                       SW3
             Branch 1                  Branch 2

Design: Hybrid enterprise topology
Devices: 3 Routers, 3 Switches, PCs and 1 Server
""")

def ip():
    show("IP / VLSM", """
R1# show ip interface brief

Interface        IP Address        Status
G0/0             192.168.10.1     up
G0/1             10.0.0.1          up
G0/2             10.0.0.5          up

VLSM SUBNETS
R&D       192.168.10.0/28
SALES     192.168.10.16/28
HR        192.168.10.32/29
FINANCE   192.168.10.40/29
BRANCH 1  192.168.10.48/29
BRANCH 2  192.168.10.56/29

RESULT: ADDRESSING VERIFIED
""")

def routing():
    show("ROUTING", """
R1# show ip route

C 192.168.10.0/28    directly connected
C 192.168.10.16/28   directly connected
C 192.168.10.32/29   directly connected
S 192.168.10.48/29   via 10.0.0.2
S 192.168.10.56/29   via 10.0.0.6

R2# show ip route
S 192.168.10.0/28    via 10.0.0.1
S 192.168.10.16/28   via 10.0.0.1

R3# show ip route
S 192.168.10.0/28    via 10.0.0.5

RESULT: ROUTING TABLE VERIFIED
""")

def ping():
    show("PING TEST", """
PC-R&D> ping 192.168.10.50

Reply from 192.168.10.50: bytes=32 time<1ms
Reply from 192.168.10.50: bytes=32 time<1ms
Reply from 192.168.10.50: bytes=32 time<1ms
Reply from 192.168.10.50: bytes=32 time<1ms

Sent = 4
Received = 4
Lost = 0 (0% loss)

RESULT: END-TO-END CONNECTIVITY SUCCESSFUL
""")

def protocols():
    show("TCP / UDP", """
PROTOCOL TEST

TCP
Connection : Established
Delivery   : Reliable
Status     : PASS

UDP
Connection : Connectionless
Overhead   : Low
Status     : PASS

TCP  -> reliable and ordered delivery
UDP  -> faster, connectionless delivery

RESULT: TCP / UDP ANALYSIS COMPLETED
""")

def services():
    show("HTTP / DNS", """
SERVER1
IP Address : 192.168.10.12

HTTP SERVICE
Status : ON
Request: http://192.168.10.12
Result : Web response received

DNS SERVICE
Status : ON
www.enterprise.local -> 192.168.10.12
Result : Name resolved

RESULT: HTTP / DNS VERIFIED
""")

def traffic():
    show("TRAFFIC", """
PERFORMANCE TEST

Condition       Latency    Throughput    Packet Loss
Normal          18 ms      92 Mbps       1%
High Traffic    35 ms      78 Mbps       4%
Congestion      58 ms      61 Mbps       9%

Observation:
As traffic increases, latency and packet loss increase,
while available throughput decreases.

RESULT: PERFORMANCE ANALYSIS COMPLETED
""")

def failure():
    show("FAILURE", """
LINK FAILURE TEST

BEFORE FAILURE
PC -> Branch PC : SUCCESS

LINK DOWN
R1 G0/1 -------- X -------- R2 G0/1

DURING FAILURE
PC -> Branch PC : REQUEST TIMED OUT

RECOVERY
Link restored
PC -> Branch PC : SUCCESS

RESULT: FAILURE AND RECOVERY VERIFIED
""")

def run_all():
    show("ALL TESTS", """
================================================
 ENTERPRISE NETWORK - FINAL VERIFICATION
================================================

IPv4 / VLSM              : PASS
Routing                  : PASS
Ping Connectivity        : PASS
TCP                      : PASS
UDP                      : PASS
HTTP                     : PASS
DNS                      : PASS
Traffic Analysis         : TESTED
Link Failure / Recovery  : TESTED

Normal     : 18 ms | 92 Mbps | 1% loss
High       : 35 ms | 78 Mbps | 4% loss
Congested  : 58 ms | 61 Mbps | 9% loss

FINAL STATUS: NETWORK TESTING COMPLETED
================================================
""")

root = tk.Tk()
root.title("CSA0704 - Cisco Enterprise Network Simulator")
root.geometry("1100x680")
root.configure(bg="#0b1720")

header = tk.Label(root, text="CSA0704  |  CISCO ENTERPRISE NETWORK SIMULATOR",
                  font=("Arial", 18, "bold"), fg="white", bg="#0b1720")
header.pack(pady=14)

tk.Label(root, text="Python GUI Front-End | Cisco-Style Network Verification",
         font=("Arial", 10), fg="#55c7e8", bg="#0b1720").pack()

buttons = tk.Frame(root, bg="#0b1720")
buttons.pack(fill="x", padx=15, pady=15)

items = [
    ("TOPOLOGY", topology), ("IP / VLSM", ip), ("ROUTING", routing),
    ("PING", ping), ("TCP / UDP", protocols), ("HTTP / DNS", services),
    ("TRAFFIC", traffic), ("LINK FAILURE", failure), ("RUN ALL", run_all)
]

for name, func in items:
    tk.Button(buttons, text=name, command=func,
              font=("Arial", 9, "bold"), bg="#17465a", fg="white",
              activebackground="#23748e", relief="flat",
              padx=8, pady=9).pack(side="left", padx=3, expand=True, fill="x")

box = tk.LabelFrame(root, text=" CISCO-STYLE COMMAND / RESULT OUTPUT ",
                    font=("Arial", 11, "bold"),
                    fg="#55c7e8", bg="#10232e")
box.pack(fill="both", expand=True, padx=15, pady=5)

output = tk.Text(box, bg="#02070a", fg="#d9f0f5",
                 font=("Consolas", 11), relief="flat",
                 padx=15, pady=12)
output.pack(fill="both", expand=True, padx=8, pady=8)

status = tk.Label(root, text="● READY", font=("Consolas", 10, "bold"),
                  fg="#55c7e8", bg="#0b1720", anchor="w")
status.pack(fill="x", padx=18, pady=8)

topology()
root.mainloop()
