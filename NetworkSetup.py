class Network( Topo ):

    def __init__( self, numberOfdevices, numberOfSwitches ):
       
        # Initialize topology
        Topo.__init__( self )
        
        #list to store all the switches
        switches = []
        
        # Add switches where each switch represents a group of nodes connected together
        # In real time there might be multiple groups requiring multiple switches
        
        for i in range(numberOfSwitches):
            switch = self.addSwitch('s' + str(i))
            switches.add(switch)
            
        # Add hosts balance equally between switches
        for i in range(numberOfSwitches):
            for j in range(numberOfDevices/numberOfSwitches):  # dividing by numberOfSwitches to equally distribute between switches.
                newHost = self.addHost( 'h' + str(i + j) )
                
                #add link
                self.addLink(newHost, switches[i])
            

        # Add links between switches
        for i in range(numberOfSwitches):
            self.addLink( switches[i], switches[i + 1] )


topos = { 'mytopo': ( lambda: Network() ) }
