addresses = []
addresses.append("012.2.21.1")
addresses.append("90:9:8")
addresses.append(":::9:9")
addresses.append("0000:0000:0001")
addresses.append("2001:db8:::ff00:42:8329")

def validateAddresses(addresses):
    for i in range(len(addresses)):
        is_ipv4 = True
        if '.' in addresses[i]:
            nums = addresses[i].split('.')
            if len(nums) > 4:#
                is_ipv4 = False
            else:
                for j in range(len(nums)):
                    if(len(nums[j])>3):
                        is_ipv4 = False
                    else:
                        if(nums[j][0] == '0'):
                            for k in range(len(nums[j])):
                                if(nums[j][k] > '8'):
                                    is_ipv4 = False
                                    break
                                    print(nums[j])
                        else:
                            if(eval(nums[j]) > 255):
                                is_ipv4 = False
                                break
            if is_ipv4 == True:
                addresses[i] = "IPv4"
            elif is_ipv4 == False:
                addresses[i] ="Neither"

        elif ':' in addresses[i]:
            is_ipv6 = True
            nums = addresses[i].split(':')

            maohao = 0
            for j in range(len(nums) - 1):
                if nums[j] == "" and nums[j + 1] == "":
                    maohao+=1
            if maohao > 1:
                is_ipv6 = False

            if len(nums) > 8:
                is_ipv6 = False
            else:
                for j in range(len(nums)):
                    if len(nums[j]) > 4:
                        is_ipv6 = False
                        break
                    elif 0 < len(nums[j]) < 4 and nums[j][0] == '0':
                        is_ipv6 = False
                        break
                    else:
                        for k in range(len(nums[j])):
                            if(not ('0' <= nums[j][k] <= '9' or 'a' <= nums[j][k] <= 'f')):
                                is_ipv6 = False
                                break
            if is_ipv6 == True:
                addresses[i] = "IPv6"
            elif is_ipv6 == False:
                addresses[i] = "Neither"
        else:
            addresses[i] = "Neither"
    return addresses

print(validateAddresses(addresses))