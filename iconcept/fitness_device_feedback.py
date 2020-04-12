class FitnessDeviceFeedback:
    distance=0.0
    speed=0.0
    time=0
    calorie=0
    watt=0
    incline=0
    pulse=0
    rpm=0

    def __init__(self,message:str):
        # 20 hex chars = 10 bytes in message
        # 
        byte_array = [message[i: i + 2] for i in range(0, len(message), 2)]
        self.time=int(byte_array[0]+byte_array[1],16)
        distance_x=int(byte_array[2],16)
        distance_y=int(byte_array[3],16)
        self.calorie=int(byte_array[4]+byte_array[5],16)
        speed_x=int(byte_array[6],16)
        speed_y=int(byte_array[7],16)
        self.incline=int(byte_array[8],16)
        self.pulse=int(byte_array[9],16)
        self.distance=round(float(distance_x)+(float(distance_y)/100),2)
        self.speed=round(float(speed_x)+(float(speed_y/100)),2)
        
        

        
        '''
            statistic.time = bb.getShort(); 01
            byte distanceX = bb.get();2
            byte distanceY = bb.get();3
            statistic.calorie = bb.getShort();45
            byte speedX = bb.get();6
            byte speedY = bb.get();7
            statistic.incline = bb.get();8
            statistic.pulse = bb.get() & 0xFF;9
        '''