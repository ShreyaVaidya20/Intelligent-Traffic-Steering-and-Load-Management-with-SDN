
from mininet.topo import Topo

class MyTopo(Topo):
    "Custom SDN topology for traffic steering and load balancing."

    def build(self):

        # Hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        # Switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')

        # Network Links
        self.addLink(h1, s1)
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s3, s5)
        self.addLink(s5, s4)
        self.addLink(s2, s4)
        self.addLink(s4, h2)

topos = {'simple_topo': (lambda: MyTopo())}