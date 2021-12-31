#message1="D2FE28"
#message2="38006F45291200"
#message3="EE00D40C823060"
#messages=["8A004A801A8002F478","620080001611562C8802118E34","C0015000016115A2E0802F182340","A0016C880162017C3686B18A3D4780"]
messages=["9C0141080250320F1802104A08"]

def day16(hexMessage):
    message=hexToBin(hexMessage)
    print('hex, bin:', hexMessage, message)

    ver,result,body=parseBody(message)

    print('ver, result, body:', ver, result, body)

def parseBody(message):
    ver,type,body=splitPacket(message)
    print('ver, type, body:', ver, type, message)

    if type == 4:
        lit,body=getLiteral(body)
        print('literal:', lit,body)
        return ver,lit,body
    else:
        lengthType, length, body = getOperator(body)
        print('operator - lenType, len, body:', lengthType, length, body)

        tempValues=[]

        if lengthType == '0':
            # packets by bit size
            bitBody = body[:length]
            while len(bitBody) > 0:
                ver,result,bitBody=parseBody(bitBody)
                tempValues.append(result)
            body=body[length:]
        else:
            # packets by count
            for i in range(0, length):
                ver,result,body=parseBody(body)
                tempValues.append(result)

        result = 0
        if type == 0:
            for t in tempValues:
                result += t
        elif type == 1:
            result=1
            for t in tempValues:
                result *= t
        elif type == 2:
            result = tempValues[0]
            for t in tempValues:
                if t < result:
                    result = t
        elif type == 3:
            result = tempValues[0]
            for t in tempValues:
                if t > result:
                    result = t
        elif type == 5:
            if tempValues[0]>tempValues[1]:
                result = 1
        elif type == 6:
            if tempValues[0]<tempValues[1]:
                result = 1
        elif type == 7:
            if tempValues[0] == tempValues[1]:
                result = 1

        return ver,result,body

def hexToBin(hex, padZeros=True):
    binMessage=bin(int(hex, 16))
    return binMessage[2:].zfill(len(hex)*4) if padZeros else hex[2:]

def hexToDec(hex):
    return int(hex, 16)

def binToDec(ver):
    return int(ver, 2)

def splitPacket(message):
    ver=binToDec(message[0:3])
    type=binToDec(message[3:6])
    return ver, type, message[6:]

def getLiteral(message):
    lastUnit = False
    theNumberInBin = ''

    while not lastUnit:
        lastUnit = message[0] == '0'
        theNumberInBin += message[1:5]
        message = message[5:]

    lit=binToDec(theNumberInBin)
    return lit,message

def getOperator(message):
    lengthType=message[0]
    bitCount = 15 if lengthType == '0' else 11
    length=message[1:bitCount+1]

    return lengthType,binToDec(length),message[bitCount+1:]


for message in messages:
    print()
    print()
    day16(message)

finalMessage="4054460802532B12FEE8B180213B19FA5AA77601C010E4EC2571A9EDFE356C7008E7B141898C1F4E50DA7438C011D005E4F6E727B738FC40180CB3ED802323A8C3FED8C4E8844297D88C578C26008E004373BCA6B1C1C99945423798025800D0CFF7DC199C9094E35980253FB50A00D4C401B87104A0C8002171CE31C41201062C01393AE2F5BCF7B6E969F3C553F2F0A10091F2D719C00CD0401A8FB1C6340803308A0947B30056803361006615C468E4200E47E8411D26697FC3F91740094E164DFA0453F46899015002A6E39F3B9802B800D04A24CC763EDBB4AFF923A96ED4BDC01F87329FA491E08180253A4DE0084C5B7F5B978CC410012F9CFA84C93900A5135BD739835F00540010F8BF1D22A0803706E0A47B3009A587E7D5E4D3A59B4C00E9567300AE791E0DCA3C4A32CDBDC4830056639D57C00D4C401C8791162380021108E26C6D991D10082549218CDC671479A97233D43993D70056663FAC630CB44D2E380592FB93C4F40CA7D1A60FE64348039CE0069E5F565697D59424B92AF246AC065DB01812805AD901552004FDB801E200738016403CC000DD2E0053801E600700091A801ED20065E60071801A800AEB00151316450014388010B86105E13980350423F447200436164688A4001E0488AC90FCDF31074929452E7612B151803A200EC398670E8401B82D04E31880390463446520040A44AA71C25653B6F2FE80124C9FF18EDFCA109275A140289CDF7B3AEEB0C954F4B5FC7CD2623E859726FB6E57DA499EA77B6B68E0401D996D9C4292A881803926FB26232A133598A118023400FA4ADADD5A97CEEC0D37696FC0E6009D002A937B459BDA3CC7FFD65200F2E531581AD80230326E11F52DFAEAAA11DCC01091D8BE0039B296AB9CE5B576130053001529BE38CDF1D22C100509298B9950020B309B3098C002F419100226DC"
day16(finalMessage)