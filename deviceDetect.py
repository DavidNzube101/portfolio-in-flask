def detectDeviceType(theRequest):
    user_agent = theRequest.user_agent.string.lower()

    if 'mobile' in user_agent:
        device_type = 'Mobile'

        if 'android' in user_agent:
            device_type = "Mobile Android"

        if 'iphone' in user_agent:
            device_type = "Mobile iOS"

    else:
        device_type = 'Desktop'

    return device_type

if __name__ == '__main__':
    pass