password = "HCBTSXWCRQGLES"

chiphrtext = [2,5,1,3,6,4,9,7,8,14,10,13,11,12]

runner = ["ZWAXJGDLUBVIQHKYPNTCRMOSFE",
          "KPBELNACZDTRXMJQOYHGVSFUWI",
          "BDMAIZVRNSJUWFHTEQGYXPLOCK",
          "RPLNDVHGFCUKTEBSXQYIZMJWAO",
          "IHFRLABEUOTSGJVDKCPMNZQWXY",
          "AMKGHIWPNYCJBFZDRUSLOQXVET",
          "GWTHSPYBXIZULVKMRAFDCEONJQ",
          "NOZUTWDCVRJLXKISEFAPMYGHBQ",
          "QWATDSRFHENYVUBMCOIKZGJXPL",
          "WABMCXPLTDSRJQZGOIKFHENYVU",
          "XPLTDAOIKFZGHENYSRUBMCQWVJ",
          "TDSWAYXPLVUBOIKZGJRFHENMCQ",
          "BMCSRFHLTDENQWAOXPYVUIKZGJ",
          "XPHKZGJTDSENYVUBMLAOIRFCQW",
          ]

chirunner = []

for i in range(14):
    
    chirunner.append(runner[chiphrtext[i]-1])
    print (chirunner[i])

print("----------------------------")

for i in range(14):

    while True:

        if chirunner[i][0:1] == password[i]:

            print(chirunner[i])

            break
        
        chirunner[i] = chirunner[i][1:]+chirunner[i][0:1]








