# Project 21: SDN Topology Change Detector

##  Problem Statement
Implement an SDN controller module using Ryu that dynamically detects and logs changes in network topology (such as switches joining/leaving or links going up/down) by monitoring LLDP (Link Layer Discovery Protocol) and OpenFlow `PORT_STATUS` messages.

##  Prerequisites
* **Mininet** (Network Emulator)
* **Ryu** (OpenFlow SDN Controller)
* **TShark** (Terminal-based Packet Analyzer)
* **Python 3**

##  Execution Steps

**1. Start the Ryu Controller** Run the controller script with the `--observe-links` flag enabled so it actively sends out LLDP discovery packets:
```bash
ryu-manager --observe-links detector.py
````

**2. Start the Mininet Topology** Launch the custom triangle topology and connect it to the remote controller:

```bash
sudo mn --custom dynamic_topo.py --topo triangle --mac --controller=remote,ip=127.0.0.1,port=6653
```

**3. Monitor Network Traffic** Use TShark to listen for OpenFlow port status changes on the network:

```bash
sudo tshark -i any -l | grep "PORT_STATUS"
```

**4. Trigger a Topology Change** In the Mininet CLI, explicitly bring down a link to simulate a severed cable:

```bash
mininet> link s1 s2 down
```

-----

## 📸 Proof of Execution

### 1\. Triggering the Event (Mininet)

*Dropping the link between Switch 1 and Switch 2 to simulate a network hardware failure.*

### 2\. Controller Detection (Ryu)

*The custom Ryu controller script successfully parses the OpenFlow messages and logs the specific `Link Down` event without crashing the network.*

### 3\. Packet-Level Verification (TShark)

*TShark intercepts the raw OpenFlow packet, proving the switch transmitted an `OFPT_PORT_STATUS` message to notify the controller of the severed link.*

```
