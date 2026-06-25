## Traffic Steering and Load Balancing


This work presents an SDN-based Load Balancing and Traffic Steering system developed using Ryu Controller, Mininet, OpenFlow, and Python. The objective of the project is to improve network performance by dynamically distributing traffic across multiple available paths instead of relying on traditional single-path routing techniques. The network topology consists of 16 hosts and 8 switches interconnected through multiple redundant links, providing flexibility and fault tolerance.

A DFS-based path discovery algorithm is implemented to identify all possible routes between source and destination nodes and calculate path costs based on link bandwidth. The Ryu controller acts as a centralized control plane, continuously monitoring the network and dynamically installing flow rules on OpenFlow switches. Multipath load balancing is achieved using OpenFlow Group Tables, enabling efficient traffic distribution and preventing network bottlenecks.

The system also incorporates intelligent traffic steering and QoS-aware routing to select optimal paths based on network conditions, reducing latency and improving throughput. Experimental evaluation using ping and Iperf tests demonstrated successful multipath routing, zero packet loss, efficient bandwidth utilization, and reliable communication. This project highlights the advantages of Software Defined Networking in building scalable, flexible, and high-performance network infrastructures capable of adapting to dynamic traffic demands.

## Features
- Multipath Load Balancing
- Dynamic Traffic Steering
- DFS-based Path Discovery
- QoS-aware Routing
- OpenFlow Flow Management
- Centralized SDN Control

## Technologies Used
- Python
- Ryu Controller
- Mininet
- OpenFlow
- Open vSwitch (OVS)
- Linux

  ## How to Run
1. Install Mininet and Ryu.
2. Run the topology script.
3. Start the Ryu controller.
4. Execute the Mininet topology and verify connectivity.
