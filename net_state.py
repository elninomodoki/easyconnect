def net_state():  
    import os  
    ping_value=os.system('ping 8.8.8.8') 
    #print(ping_value)
    if ping_value==1:  
        print('ping fail' )
        #os.system('msdt.exe /id NetworkDiagnosticsNetworkAdapter')#调用系统网络诊断  
    else:  
        print('ping succeed') 
net_state()
