# TV controller Create a simple prototype of a TV controller in Python.It’ll use the following commands:
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel.Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel.If the current channel is the last one, turns on the first channel.previous_channel() - turns
# on the previous channel.If the current channel is the first one, turns on the last channel. current_channel() - returns the name of
# the current channel. is_exist(N / 'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",if the channel N or 'name'
# exists in the list, or "No" - in the other case.The default channel turned on before all commands is №1.Your  task is to create  the
# TVController class and methods described above.
CHANNELS_all = ["BBC", "Discovery", "TV1000","MTV","Ukraine24","Deutsche Welle"]
class Tvcontroller:
    def __init__(self,CHANNELS,num_channel=0):
        self.num_channel = num_channel
        self.CHANNELS = CHANNELS
    def first_channel(self):
        self.num_channel =0
        print('First channel:',self.num_channel+1,'channel is:',self.CHANNELS[self.num_channel])

    def last_channel(self):
        self.num_channel = len(CHANNELS_all)-1
        print('Last channel:',self.num_channel+1,'channel is:',self.CHANNELS[self.num_channel])

    def turn_channel(self,num_channel):
        self.num_channel = num_channel-1
        print('Current channel:', self.num_channel + 1, 'channel is:', self.CHANNELS[self.num_channel])

    def previous_chanel(self):
        if self.num_channel == 0:
            self.num_channel = 5
        else:
            self.num_channel -=1
        print('Previous channel:', self.num_channel + 1, 'channel is:', self.CHANNELS[self.num_channel])
    def next_chanel(self):
        if self.num_channel == 5:
            self.num_channel = 0
        else:
            self.num_channel+=1
        print('Next channel:', self.num_channel + 1, 'channel is:', self.CHANNELS[self.num_channel])
    def is_exist(self,name):
        if name in CHANNELS_all:
            print('Yes')
        else:
            print('No')




channels = Tvcontroller(CHANNELS_all)
channels.first_channel()
channels.last_channel()
channels.turn_channel(6)
channels.next_chanel()
channels.previous_chanel()
channels.is_exist("Uyt")
channels.is_exist("BBC")


