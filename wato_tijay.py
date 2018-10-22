from graphics import*
import datetime
class start:
    def main(self):
        try:
            #draw the graph win set backgroound and put an image
            win = GraphWin('Inventory',800,700)
            win.setCoords(0.0,0.0,10.0,10.0)
            win.setBackground("#FF66B2")
            img1 = Image(Point(5,5), 'Wuyeh.gif').draw(win)
            #create the log in page of the program
            def haha():
                for i in range(6):
                    Proname = Text(Point(i,9.5),'WatoTijay')
                    welcome = Text(Point(i,8.5), "Welcome to the Inventory"
                               " manager and customer's payment Calculator")
                    welcome.setFill('#ffffff')
                    welcome.setSize(15)
                    welcome.setStyle('bold')
                    welcome.draw(win)
                    Proname.setFill('blue')
                    Proname.setStyle('italic')
                    Proname.setSize(30)
                    Proname.draw(win)
                    time.sleep(0.1)
                    welcome.setText('')
                    Proname.setText('')
                Proname.setText('WatoTijay')
                welcome.setText("Welcome to the Inventory"
                               " manager and customer's payment Calculator")
                ask = Text(Point(5,6), "Enter your Username and password below")
                ask.setFill('#f0ffff')
                ask.setSize(25)
                ask.draw(win)
                SName = Entry(Point(4,5),15)
                SName.draw(win)
                SText = Text(Point(2,5), 'Shop Name')
                SText.setFill('#e0eee0')
                SText.setSize(15)
                SText.draw(win)
                Ntext = Text(Point(2,4.5), 'Username')
                Ntext.setFill('#e0eee0')
                Ntext.setSize(15)
                Ntext.draw(win)
                NEntry = Entry(Point(4,4.5),15)
                NEntry.draw(win)
                Ptext = Text(Point(2,4), 'Password')
                Ptext.setFill('#e0eee0')
                Ptext.setSize(15)
                Ptext.draw(win)
                PEntry = Entry(Point(4,4),15)
                PEntry.setText('')
                PEntry.draw(win)
                EXit = Rectangle(Point(7.8,2), Point(9,2.4))
                EXit.setFill('white')
                EXit.draw(win)
                EText = Text(Point(8.4,2.2), 'Exit')
                EText.draw(win)
                Lbutton = Rectangle(Point(3.5,3), Point(4.5,3.5))
                Lbutton.setFill('chocolate')
                Lbutton.draw(win)
                LText = Text(Point(4,3.25), 'Log In')
                LText.draw(win)
                #Lists to store the inventory
                IDs = []
                ShopItems = []
                Prices = []
                Quantities = []
                update = []
                update1 = []
                #Second page of the program
                global Inventory
                def Inventory():
                    win.setBackground("brown")
                    #write introduction on top
                    intro = Text(Point(5,9.8), 'Inventory Tracker, and Customer payment Calculator')
                    intro.setFill('yellow')
                    intro.setSize(18)
                    intro.setStyle('bold')
                    intro.setFace('courier')
                    intro.draw(win)
                    #Draw the horizontal line on top
                    line1 = Line(Point(0,9.3), Point(10,9.3))
                    line1.draw(win)
                    #draw the entry point of the text file
                    fileName = Text(Point(1,9.5), 'Enter file Name:')
                    fileName.setFill('yellow')
                    fileName.setStyle('bold')
                    fileName.draw(win)
                    global FEntry
                    FEntry = Entry(Point(2.8,9.5), 15)
                    FEntry.setText('')
                    FEntry.draw(win)
                    #draw logout button
                    LO1 = Rectangle(Point(8.9,9.4), Point(9.7,9.7))
                    LO1.setFill('white')
                    LO1.draw(win)
                    LOT1 = Text(Point(9.3,9.55), 'Log Out')
                    LOT1.draw(win)
                    #create enter button beside the rntry point
                    Ebutton = Rectangle(Point(4,9.2),Point(5,9.7))
                    Ebutton.setFill('pink')
                    Ebutton.draw(win)
                    Etext = Text(Point(4.5,9.5), 'Enter')
                    Etext.draw(win)
                    #draw the vertical line
                    line2 = Line(Point(7,9.3), Point(7,0))
                    line2.draw(win)
                    #draw the two lines from generate receipt to quit button
                    line4 = Line(Point(7.2,8.8), Point(7.8,2.4))
                    line4.draw(win)
                    line5 = Line(Point(9.8,8.8), Point(9,2.4))
                    line5.draw(win)
                    #draw the  space for items
                    confirm =  Rectangle(Point(0,0), Point(7,9.3))
                    confirm.setFill('#00ffff')
                    confirm.draw(win)
                    #draw two buttons and the top right hand corner
                    z = 8.8
                    f = 9.2
                    g = ['#00ffff','pink']
                    for i in range(2):
                        Rbutton = Rectangle(Point(7.2,z), Point(9.8,f))
                        Rbutton.setFill(g[i])
                        Rbutton.draw(win)
                        z = z - 0.4
                        f =  f - 0.4
                    #write the text of the two buttons at the top right hand corner
                    Ctext = Text(Point(8.5,9), 'Available Items')
                    Ctext.draw(win)
                    Rtext = Text(Point(8.5,8.6), 'sell to customer')
                    Rtext.draw(win)
                    #create quit button and put the text inside
                    Quit = Rectangle(Point(7.8,2), Point(9,2.4))
                    Quit.setFill('white')
                    Quit.draw(win)
                    Qtext = Text(Point(8.4,2.2), 'Quit')
                    Qtext.draw(win)
                    #write a text at the space where shop items will be displayed
                    direct = Text(Point(3.5,6), 'Your Shop Items will be displayed here ')
                    direct.setSize(17)
                    direct.setFace('courier')
                    direct.setStyle('bold')
                    direct.draw(win)
                    #draw the gambian flag and put text in the middle
                    a = 0
                    b = 0.38
                    c = ['green','white','blue','white','red']
                    for i in range(5):
                        flag = Rectangle(Point(7.1,a), Point(9.9,b))
                        flag.setFill(c[i])
                        flag.draw(win)
                        a = a + 0.38
                        b = b + 0.38
                    name = Text(Point(8.5,1),'I love The Gambia')
                    name.setFace('courier')
                    name.draw(win)
                    #Take care of the mouse clicks and make sure they can be clicked again
                    #Prevent clicking outside the buttons
                    global MClick
                    def MClick():
                        IT = win.getMouse()
                        if 7.2 <= IT.getX() <= 9.8 and 8.4<= IT.getY()<=8.8:
                            FEntry.undraw()
                            sellItems()
                            MClick()
                        elif 7.2<= IT.getX()<= 9.8 and 8.8<= IT.getY()<=9.2:
                            direct.setText('')
                            showEntry()
                            MClick()
                        elif 7.8<=IT.getX()<=9 and 2<=IT.getY()<=2.4:
                            win.close()
                        elif 4<=IT.getX()<=5 and 9.3<=IT.getY()<=9.7:
                            ItemEntry()
                            MClick()
                        elif 8.9<=IT.getX()<=9.7 and 9.4<=IT.getY()<=9.7:
                            FEntry.undraw()
                            erase2 = Rectangle(Point(0,0), Point(10,10))
                            erase2.setFill('#FF66B2')
                            erase2.draw(win)
                            img1 = Image(Point(5,5), 'Wuyeh.gif').draw(win)
                            haha()
                        else:
                            NC= Text(Point(3.5,8), 'Please Click one of the Butttons')
                            NC.setSize(15)
                            NC.draw(win)
                            time.sleep(2)
                            NC.setText('')
                            MClick()
                    MClick()
                #store the items in the list
                def ItemEntry():
                    try:
                        #Open file and read its contentent
                        infile = open(FEntry.getText(), 'r')
                        Notify  = Text(Point(7,9.5), 'Items entry Successful!')
                        Notify.setSize(15)
                        Notify.setFill('red')
                        Notify.draw(win)
                        time.sleep(2)
                        Notify.setText('')
                        #split the lines without newline character. Idea taken from
                        #http://stackoverflow.com/questions/31926078/using-splitlines-in-python-to-only-get-some-lines
                        info = infile.read().splitlines()
                        # Iterates through the items in the file and store them in the arrays
                        for line in info:
                            chars = line.split(' ')
                            #Delete the empty spaace if the user puts an extra space
                            def delete():
                                for a in chars:
                                    if a=='':
                                        chars.remove(a)
                                        delete()
                                    if a==',':
                                        chars.remove(a)
                                        delete()
                                    if a==', ':
                                        chars.remove(a)
                                        delete()
                            delete()

                            iD = chars[0]
                            item = chars[1]
                            price = chars[2]
                            quantity= chars[3]
                            IDs.append(iD)
                            ShopItems.append(item)
                            Prices.append(price)
                            Quantities.append(quantity)
                            update.append(quantity)
                            update1.append(quantity)
                    except FileNotFoundError:
                        FE = Text(Point(3,8.5),"Recheck your file, and its directory")
                        FE.setFill('red')
                        FE.draw(win)
                        time.sleep(2)
                        FE.setText('')
                        MClick()
                #Clicking on Availble items shows the items in your list
                def showEntry():
                        column = Text(Point(3.5,9.1),'     ID                              Shop Item'
                                      '                    Price(GH¢)     Quantity Available')
                        column.setFill('yellow')
                        column.draw(win)
                        line6 = Line(Point(1,9.3), Point(1,0))
                        line6.draw(win)
                        line7 = Line(Point(4,9.3), Point(4,0))
                        line7.draw(win)
                        line8 = Line(Point(5,9.3), Point(5,0))
                        line8.draw(win)
                        d = 8.8
                        for i in range(len(IDs)):
                            Text(Point(0.5,d), IDs[i]).draw(win)
                            Text(Point(2.5,d),ShopItems[i]).draw(win)
                            Text(Point(4.5,d),Prices[i]).draw(win)
                            Text(Point(6,d),update[i]).draw(win)
                            d = d - 0.3
                #list to store the sold items
                SoldItems = []
                SiD = []
                TAmount = []
                SingleItem = []
                SingleID = []
                #Third page of the program
                def sellItems():
                    #decorate the third page
                        erase = Rectangle(Point(0,0), Point(10,10))
                        erase.setFill('#d8bfd8')
                        erase.draw(win)
                        Img = Image(Point(5,5), 'img.gif')
                        Img.draw(win)
                        Outline = Rectangle(Point(0.05,0), Point(10,9.95))
                        Outline.setOutline('#00bfff')
                        Outline.setWidth(5)
                        Outline.draw(win)
                        welcome = Text(Point(5,9), "Here are the items available,"
                                       "  their prices and Quantitities")
                        welcome.setFill('#00ffff')
                        welcome.setStyle('bold')
                        welcome.setSize(20)
                        welcome.draw(win)
                        n=v = 1
                        r = 0.5
                        u = 1.5
                        s = 1.2
                        a = 0.8
                        k =['#add8e6','#afeeee','#00ced1','#40e0d0','#87cefa','#00bfff','#87cefa','#48d1cc','#00bfff']
                        for i in range(len(k)):
                            J = Rectangle(Point(r,7.1), Point(u,8.2))
                            J.setFill(k[i])
                            J.draw(win)
                            r = r+1
                            u = u+1
                        r = 0.5
                        u = 1.5
                        for i in range(len(k)):
                            J = Rectangle(Point(u,3.5), Point(r,4.6))
                            J.setFill(k[i])
                            J.draw(win)
                            r = r+1
                            u = u+1
                        if len(ShopItems) >= 13:
                            for i in range(9):
                                T = Text(Point(n,8), ShopItems[i])
                                T.setSize(10)
                                T.draw(win)
                                n = n+1
                            for i in range(9):
                                A = Text(Point(v,7.6), update[i])
                                A.setSize(15)
                                A.draw(win)
                                v = v+1
                            for i in range(9):
                                Text(Point(a,7.3), 'GH¢').draw(win)
                                P = Text(Point(s,7.3), Prices[i])
                                P.setSize(13)
                                P.draw(win)
                                s = s+1
                                a = a+1
                            c = Circle(Point(2,6), 0.8)
                            c.setFill('#db7093')
                            c.draw(win)
                            c1 = c.clone()
                            c1.move(2,0)
                            c1.setFill('#c71585')
                            c1.draw(win)
                            c2 = c1.clone()
                            c2.move(2,0)
                            c2.setFill('#ee82ee')
                            c2.draw(win)
                            c3 = c2.clone()
                            c3.move(2,0)
                            c3.setFill('#da70d6')
                            c3.draw(win)
                            o=v=2
                            s=2.3
                            a=1.8
                            for i in range(9,13):
                                S = Text(Point(o,6.5), ShopItems[i])
                                S.setSize(10)
                                S.draw(win)
                                A = Text(Point(v,6.1), update[i])
                                A.setSize(15)
                                A.draw(win)
                                Text(Point(a,5.7), 'GH¢').draw(win)
                                P = Text(Point(s,5.7), Prices[i])
                                P.setSize(13)
                                P.draw(win)
                                s = s+2
                                a = a+2
                                v = v+2
                                o = o+2
                            s = 1.2
                            a = 0.8
                            v=n =1
                            for i in range(13,len(ShopItems)):
                                T = Text(Point(n,4.4), ShopItems[i])
                                T.setSize(10)
                                T.draw(win)
                                A = Text(Point(v,4.1), update[i])
                                A.setSize(15)
                                A.draw(win)
                                Text(Point(a,3.7), 'GH¢').draw(win)
                                P = Text(Point(s,3.7), Prices[i])
                                P.setSize(13)
                                P.draw(win)
                                s = s+1
                                a = a+1
                                v = v+1
                                n = n+1
                        elif len(ShopItems)<=9:
                            for i in range(len(ShopItems)):
                                T = Text(Point(n,8), ShopItems[i])
                                T.setSize(10)
                                T.draw(win)
                                n = n+1
                            for i in range(len(ShopItems)):
                                A = Text(Point(v,7.6), update[i])
                                A.setSize(15)
                                A.draw(win)
                                v = v+1
                            for i in range(len(ShopItems)):
                                Text(Point(a,7.3), 'GH¢').draw(win)
                                P = Text(Point(s,7.3), Prices[i])
                                P.setSize(13)
                                P.draw(win)
                                s = s+1
                                a = a+1
                        elif 9<len(ShopItems)<13:
                            for i in range(9):
                                T = Text(Point(n,8), ShopItems[i])
                                T.setSize(10)
                                T.draw(win)
                                n = n+1
                            for i in range(9):
                                A = Text(Point(v,7.6), update[i])
                                A.setSize(15)
                                A.draw(win)
                                v = v+1
                            for i in range(9):
                                Text(Point(a,7.3), 'GH¢').draw(win)
                                P = Text(Point(s,7.3), Prices[i])
                                P.setSize(13)
                                P.draw(win)
                                s = s+1
                                a = a+1
                            c = Circle(Point(2,6), 0.8)
                            c.setFill('da70d6')
                            c.draw(win)
                            c1 = c.clone()
                            c1.move(2,0)
                            c1.setFill('ba55d3')
                            c1.draw(win)
                            c2 = c1.clone()
                            c2.move(2,0)
                            c2.setFill('ee82ee')
                            c2.draw(win)
                            c3 = c2.clone()
                            c3.move(2,0)
                            c3.setFill('da70d6')
                            c3.draw(win)
                            o=v=2
                            s=2.3
                            a=1.8
                            for i in range(9,len(ShopItems)):
                                S = Text(Point(o,6.5), ShopItems[i])
                                S.setSize(10)
                                S.draw(win)
                                A = Text(Point(v,6.1), update[i])
                                A.setSize(15)
                                A.draw(win)
                                Text(Point(a,5.7), 'GH¢').draw(win)
                                P = Text(Point(s,5.7), Prices[i])
                                P.setSize(13)
                                P.draw(win)
                                s = s+2
                                a = a+2
                                v = v+2
                                o = o+2
                        #draw rectangular frame for amount to be paid
                        receipt =  Rectangle(Point(0.05,0), Point(7,3.2))
                        receipt.setOutline('green')
                        receipt.setWidth(5)
                        receipt.setFill('white')
                        receipt.draw(win)
                        #go back to item page
                        back = Rectangle(Point(7.5,2.2), Point(9.5,3))
                        back.setWidth(3)
                        back.setOutline('gray')
                        back.setFill('#ffa500')
                        back.draw(win)
                        clear = Rectangle(Point(7.5,1.2), Point(9.5,2))
                        clear.setFill('#ff6347')
                        clear.setWidth(3)
                        clear.setOutline('gray')
                        clear.draw(win)
                        HpageB = Rectangle(Point(7.5,0.2), Point(9.5,1))
                        HpageB.setFill('#fa8072')
                        HpageB.setWidth(3)
                        HpageB.setOutline('gray')
                        HpageB.draw(win)
                        Btext = Text(Point(8.5,2.6), 'Showreceipt')
                        Btext.draw(win)
                        #Create second quit button
                        Ctext = Text(Point(8.5,1.6), 'Clear Receipt')
                        Ctext.draw(win)
                        Hpage = Text(Point(8.5,0.6), 'Homepage')
                        Hpage.draw(win)
                        LO = Rectangle(Point(8.5,9.5), Point(9.3,9.8))
                        LO.setFill('#ffff00')
                        LO.draw(win)
                        LOT = Text(Point(8.9,9.65), 'Log Out')
                        LOT.draw(win)
                        Cancel = Rectangle(Point(1,8.3), Point(2,8.6))
                        Cancel.setFill('#00ff7f')
                        Cancel.draw(win)
                        CaTe= Text(Point(1.5,8.45), 'Cancel')
                        CaTe.draw(win)
                        Refresh = Rectangle(Point(8.3,8.3), Point(9.3,8.6))
                        Refresh.setFill('#00ff7f')
                        Refresh.draw(win)
                        RFtext = Text(Point(8.8,8.45),'Refresh')
                        RFtext.draw(win)
                        #draw horizontal line between shop item display position and receipt
                        line3 = Line(Point(0,3.2), Point(10,3.2))
                        line3.setWidth(5)
                        line3.setFill('#00bfff')
                        line3.draw(win)
                        #draw the columns for item sold
                        colum = Text(Point(3.2,2.7), '                 Item                 '
                                     ' Price(GH¢)              Quantity              Amount(GH¢)')
                        colum.setFill('green')
                        colum.draw(win)
                        #Create the total indication point
                        total = Text(Point(3,0.5), 'Total Amount---------------------------'
                                     '--------------------------------------')
                        total.setStyle('italic')
                        total.setFill('brown')
                        total.setSize(12)
                        total.draw(win)
                        #able to click on the buttons over and over again on the third page, and make sales to customers
                        global purchase
                        def purchase():
                            try:
                                Aa = 2.5
                                Ab = 2.5
                                Ac = 2.5
                                Ad = 2.5
                                Amount = 0
                                FP = win.getMouse()
                                if 0.5<=FP.getX()<=1.5 and 7.1<=FP.getY()<=8.2 and eval(update[0])>0:
                                    Co = Rectangle(Point(0.8,7.5), Point(1.1,7.8))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[0]= str(eval(update[0])-1)
                                    Ni= Text(Point(0.95,7.65), update[0])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[0])
                                    TAmount.append(Prices[0])
                                    SiD.append(IDs[0])
                                    update1[0]= str(eval(update1[0])-1)
                                    purchase()
                                elif 1.5<=FP.getX()<=2.5 and 7.1<=FP.getY()<=8.2 and eval(update[1])>0:
                                    Co = Rectangle(Point(1.8,7.5), Point(2.1,7.8))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[1]= str(eval(update[1])-1)
                                    Ni= Text(Point(1.95,7.65), update[1])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[1])
                                    TAmount.append(Prices[1])
                                    SiD.append(IDs[1])
                                    update1[1]= str(eval(update1[1])-1)
                                    purchase()
                                elif 2.5<=FP.getX()<=3.5 and 7.1<=FP.getY()<=8.2 and eval(update[2])>0:
                                    Co = Rectangle(Point(2.8,7.5), Point(3.1,7.8))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[2]= str(eval(update[2])-1)
                                    Ni= Text(Point(2.95,7.65), update[2])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[2])
                                    TAmount.append(Prices[2])
                                    SiD.append(IDs[2])
                                    update1[2]= str(eval(update1[2])-1)
                                    purchase()
                                elif 3.5<=FP.getX()<=4.5 and 7.1<=FP.getY()<=8.2 and eval(update[3])>0:
                                    Co = Rectangle(Point(3.8,7.5), Point(4.15,7.8))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[3]= str(eval(update[3])-1)
                                    Ni= Text(Point(3.95,7.65), update[3])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[3])
                                    TAmount.append(Prices[3])
                                    SiD.append(IDs[3])
                                    update1[3]= str(eval(update1[3])-1)
                                    purchase()
                                elif 4.5<=FP.getX()<=5.5 and 7.1<=FP.getY()<=8.2 and eval(update[4])>0:
                                    Co = Rectangle(Point(4.8,7.5), Point(5.15,7.8))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[4]= str(eval(update[4])-1)
                                    Ni= Text(Point(4.95,7.65), update[4])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[4])
                                    TAmount.append(Prices[4])
                                    SiD.append(IDs[4])
                                    update1[4]= str(eval(update1[4])-1)
                                    purchase()
                                elif 5.5<=FP.getX()<=6.5 and 7.1<=FP.getY()<=8.2 and eval(update[5])>0:
                                    Co = Rectangle(Point(5.8,7.5), Point(6.15,7.8))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[5]= str(eval(update[5])-1)
                                    Ni= Text(Point(5.95,7.65), update[5])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[5])
                                    TAmount.append(Prices[5])
                                    SiD.append(IDs[5])
                                    update1[5]= str(eval(update1[5])-1)
                                    purchase()
                                elif 6.5<=FP.getX()<=7.5 and 7.1<=FP.getY()<=8.2 and eval(update[6])>0:
                                    Co = Rectangle(Point(6.8,7.5), Point(7.15,7.8))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[6]= str(eval(update[6])-1)
                                    Ni= Text(Point(6.95,7.65), update[6])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[6])
                                    TAmount.append(Prices[6])
                                    SiD.append(IDs[6])
                                    update1[6]= str(eval(update1[6])-1)
                                    purchase()
                                elif 7.5<=FP.getX()<=8.5 and 7.1<=FP.getY()<=8.2 and eval(update[7])>0:
                                    Co = Rectangle(Point(7.8,7.5), Point(8.15,7.8))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[7]= str(eval(update[7])-1)
                                    Ni= Text(Point(7.95,7.65), update[7])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[7])
                                    TAmount.append(Prices[7])
                                    SiD.append(IDs[7])
                                    update1[7]= str(eval(update1[7])-1)
                                    purchase()
                                elif 8.5<=FP.getX()<=9.5 and 7.1<=FP.getY()<=8.2 and eval(update[8])>0:
                                    Co = Rectangle(Point(8.8,7.5), Point(9.15,7.8))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[8]= str(eval(update[8])-1)
                                    Ni= Text(Point(8.95,7.65), update[8])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[8])
                                    TAmount.append(Prices[8])
                                    SiD.append(IDs[8])
                                    update1[8]= str(eval(update1[8])-1)
                                    purchase()
                                elif 1.2<=FP.getX()<=2.8 and 5.2<=FP.getY()<=6.8 and eval(update[9])>0:
                                    Co = Rectangle(Point(1.8,5.85), Point(2.2,6.2))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[9]= str(eval(update[9])-1)
                                    Ni= Text(Point(2,6), update[9])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[9])
                                    TAmount.append(Prices[9])
                                    SiD.append(IDs[9])
                                    update1[9]= str(eval(update1[9])-1)
                                    purchase()
                                elif 3.2<=FP.getX()<=4.8 and 5.2<=FP.getY()<=6.8 and eval(update[10])>0:
                                    Co = Rectangle(Point(3.8,5.85), Point(4.2,6.2))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[10]= str(eval(update[10])-1)
                                    Ni= Text(Point(4,6), update[10])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[10])
                                    TAmount.append(Prices[10])
                                    SiD.append(IDs[10])
                                    update1[10]= str(eval(update1[10])-1)
                                    purchase()
                                elif 5.2<=FP.getX()<=6.8 and 5.2<=FP.getY()<=6.8 and eval(update[11])>0:
                                    Co = Rectangle(Point(5.8,5.85), Point(6.2,6.2))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[11]= str(eval(update[11])-1)
                                    Ni= Text(Point(6,6), update[11])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[11])
                                    TAmount.append(Prices[11])
                                    SiD.append(IDs[11])
                                    update1[11]= str(eval(update1[11])-1)
                                    purchase()
                                elif 7.2<=FP.getX()<=8.8 and 5.2<=FP.getY()<=6.8 and eval(update[12])>0:
                                    Co = Rectangle(Point(7.8,5.85), Point(8.2,6.2))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[12]= str(eval(update[12])-1)
                                    Ni= Text(Point(8,6), update[12])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[12])
                                    TAmount.append(Prices[12])
                                    SiD.append(IDs[12])
                                    update1[12]= str(eval(update1[12])-1)
                                    purchase()

                                elif 0.5<=FP.getX()<=1.5 and 3.5<=FP.getY()<=4.6 and eval(update[13])>0:
                                    Co = Rectangle(Point(0.8,3.9), Point(1.15,4.2))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[13]= str(eval(update[13])-1)
                                    Ni= Text(Point(0.95,4.05), update[13])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[13])
                                    TAmount.append(Prices[13])
                                    SiD.append(IDs[13])
                                    update1[13]= str(eval(update1[13])-1)
                                    purchase()
                                elif 1.5<=FP.getX()<=2.5 and 3.5<=FP.getY()<=4.6 and eval(update[14])>0:
                                    Co = Rectangle(Point(1.8,3.9), Point(2.15,4.2))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[14]= str(eval(update[14])-1)
                                    Ni= Text(Point(1.95,4.05), update[14])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[14])
                                    TAmount.append(Prices[14])
                                    SiD.append(IDs[14])
                                    update1[14]= str(eval(update1[14])-1)
                                    purchase()
                                elif 2.5<=FP.getX()<=3.5 and 3.5<=FP.getY()<=4.6 and eval(update[15])>0:
                                    Co = Rectangle(Point(2.8,3.9), Point(3.15,4.2))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[15]= str(eval(update[15])-1)
                                    Ni= Text(Point(2.95,4.05), update[15])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[15])
                                    TAmount.append(Prices[15])
                                    SiD.append(IDs[15])
                                    update1[15]= str(eval(update1[15])-1)
                                    purchase()
                                elif 3.5<=FP.getX()<=4.5 and 3.5<=FP.getY()<=4.6 and eval(update[16])>0:
                                    Co = Rectangle(Point(3.8,3.9), Point(4.15,4.2))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[16]= str(eval(update[16])-1)
                                    Ni= Text(Point(3.95,4.05), update[16])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[16])
                                    SiD.append(IDs[16])
                                    TAmount.append(Prices[16])
                                    update1[16]= str(eval(update1[16])-1)
                                    purchase()
                                elif 4.5<=FP.getX()<=5.5 and 3.5<=FP.getY()<=4.6 and eval(update[17])>0:
                                    Co = Rectangle(Point(4.8,3.9), Point(5.15,4.2))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[17]= str(eval(update[17])-1)
                                    Ni= Text(Point(4.95,4.05), update[17])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[17])
                                    TAmount.append(Prices[17])
                                    SiD.append(IDs[17])
                                    update1[17]= str(eval(update1[17])-1)
                                    purchase()
                                elif 5.5<=FP.getX()<=6.5 and 3.5<=FP.getY()<=4.6 and eval(update[18])>0:
                                    Co = Rectangle(Point(5.8,3.9), Point(6.15,4.2))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[18]= str(eval(update[18])-1)
                                    Ni= Text(Point(5.95,4.05), update[18])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[18])
                                    TAmount.append(Prices[18])
                                    SiD.append(IDs[18])
                                    update1[18]= str(eval(update1[18])-1)
                                    purchase()
                                elif 6.5<=FP.getX()<=7.5 and 3.5<=FP.getY()<=4.6 and eval(update[19])>0:
                                    Co = Rectangle(Point(6.8,3.9), Point(7.15,4.2))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[19]= str(eval(update[19])-1)
                                    Ni= Text(Point(6.95,4.05), update[19])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[19])
                                    TAmount.append(Prices[19])
                                    SiD.append(IDs[19])
                                    update1[19]= str(eval(update1[19])-1)
                                    purchase()
                                elif 7.5<=FP.getX()<=8.5 and 3.5<=FP.getY()<=4.6 and eval(update[20])>0:
                                    Co = Rectangle(Point(7.8,3.9), Point(8.15,4.2))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[20]= str(eval(update[20])-1)
                                    Ni= Text(Point(7.95,4.05), update[20])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[20])
                                    TAmount.append(Prices[20])
                                    SiD.append(IDs[20])
                                    update1[20]= str(eval(update1[20])-1)
                                    purchase()
                                elif 8.5<=FP.getX()<=9.5 and 3.5<=FP.getY()<=4.6 and eval(update[21])>0:
                                    Co = Rectangle(Point(8.8,3.9), Point(9.15,4.2))
                                    Co.setFill('white')
                                    Co.draw(win)
                                    update[21]= str(eval(update[21])-1)
                                    Ni= Text(Point(8.95,4.05), update[21])
                                    Ni.draw(win)
                                    SoldItems.append(ShopItems[21])
                                    TAmount.append(Prices[21])
                                    SiD.append(IDs[21])
                                    update1[21]= str(eval(update1[21])-1)
                                    purchase()
                                elif 7.5<=FP.getX()<=9.5 and 2.2<=FP.getY()<=3:
                                    for anItem in SoldItems:
                                        if anItem not in SingleItem:
                                            SingleItem.append(anItem)
                                    for i in range(len(TAmount)):
                                        Amount = Amount + eval(TAmount[i])
                                    for anID in SiD:
                                        if anID not in SingleID:
                                            SingleID.append(anID)
                                    for i in range(len(SingleItem)):
                                        Text(Point(1,Aa),SingleItem[i]).draw(win)
                                        Text(Point(2.5,Ab), eval(Prices[eval(SingleID[i])-1])).draw(win)
                                        Rquant = eval(Quantities[eval(SingleID[i])-1])-eval(update1[eval(SingleID[i])-1])
                                        Text(Point(4.2,Ac), Rquant).draw(win)
                                        Text(Point(6,Ad), format(Rquant * eval(Prices[eval(SingleID[i])-1]),'.2f')).draw(win)
                                        Aa = Aa-0.2
                                        Ab = Ab-0.2
                                        Ac = Ac-0.2
                                        Ad = Ad-0.2
                                    time1 = Text(Point(5,3), datetime.datetime.strftime(datetime.datetime.now(), 'Time: %H:%M:%S  Date: %d-%m-%Y'))
                                    time1.draw(win)
                                    FAmount = Text(Point(6,0.5), format(Amount,'.2f'))
                                    FAmount.draw(win)
                                    Text(Point(2,3), SName.getText()).draw(win)
                                    purchase()
                                elif 7.5<=FP.getX()<=9.5 and 1.2<=FP.getY()<=2:
                                    receipt =  Rectangle(Point(0.05,0), Point(7,3.2))
                                    receipt.setOutline('green')
                                    receipt.setWidth(5)
                                    receipt.setFill('white')
                                    receipt.draw(win)
                                    colum = Text(Point(3.2,2.7), '                 Item                 '
                                         ' Price(GH¢)              Quantity              Amount(GH¢)')
                                    colum.setFill('green')
                                    colum.draw(win)
                                    #Create the total indication point
                                    total = Text(Point(3,0.5), 'Total Amount---------------------------'
                                                 '--------------------------------------')
                                    total.setStyle('italic')
                                    total.setFill('brown')
                                    total.setSize(12)
                                    total.draw(win)
                                    #deletes items from the list. Idea from
                                    #http://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index-in-python
                                    del SoldItems[:]
                                    del SiD[:]
                                    del TAmount[:]
                                    del SingleItem[:]
                                    del SingleID[:]
                                    del update1[:]
                                    for aQuant in Quantities:
                                       update1.append(aQuant)
                                    purchase()
                                elif 7.5 <= FP.getX()<=9.5 and 0.2<=FP.getY()<=1:
                                    erase = Rectangle(Point(0,0), Point(10,10))
                                    erase.setFill('brown')
                                    erase.draw(win)
                                    img1 = Image(Point(5,5), 'Wuyeh.gif').draw(win)
                                    Inventory()
                                elif 8.5<=FP.getX()<=9.3 and 9.5<=FP.getY()<=9.8:
                                    erase2 = Rectangle(Point(0,0), Point(10,10))
                                    erase2.setFill('#FF66B2')
                                    erase2.draw(win)
                                    img1 = Image(Point(5,5), 'Wuyeh.gif').draw(win)
                                    haha()
                                elif 1<=FP.getX()<=2 and 8.3<=FP.getY()<=8.6:
                                    CNote = Text(Point(5,8.45), " 1 {0:1}  is cancelled. click refresh to see effects".format(ShopItems[eval(SiD[-1])-1]))
                                    CNote.setFill('orange')
                                    CNote.setSize(14)
                                    CNote.setFace('arial')
                                    CNote.draw(win)
                                    time.sleep(1)
                                    CNote.setText('')
                                    update[eval(SiD[-1])-1]= str(eval(update[eval(SiD[-1])-1])+1)
                                    update1[eval(SiD[-1])-1]= str(eval(update1[eval(SiD[-1])-1])+1)
                                    del SoldItems[-1]
                                    del SiD[-1]
                                    del TAmount[-1]
                                    purchase()
                                elif 8.3<=FP.getX()<=9.3 and 8.3<=FP.getY()<=8.6:
                                    sellItems()

                                else:
                                    SIB = Text(Point(5,5), 'Please click on a button')
                                    SIB.setFill('yellow')
                                    SIB.setSize(25)
                                    SIB.setStyle('bold')
                                    SIB.draw(win)
                                    time.sleep(2)
                                    SIB.setText('')
                                    purchase()
                                purchase()
                            except IndexError:
                                IB = Text(Point(5,5), 'No Item')
                                IB.setSize(30)
                                IB.setFill('white')
                                IB.draw(win)
                                time.sleep(2)
                                IB.setText('')
                                purchase()
                        purchase()
                global LogIn
                def LogIn():
                    w = win.getMouse()
                    if 3.5<=w.getX()<=4.5 and 3<=w.getY()<=3.5:
                        if NEntry.getText()== 'Wuyeh' and PEntry.getText()=="1234":
                            Loading = Text(Point(5,2.5), 'loading')
                            Loading.setSize(20)
                            Loading.setFill('yellow')
                            Loading.draw(win)
                            LI = Circle(Point(5,2),0.2)
                            LI.setWidth(5)
                            LI.setOutline('yellow')
                            LI.draw(win)
                            time.sleep(3)
                            Proname.undraw()
                            welcome.undraw()
                            ask.undraw()
                            Ntext.undraw()
                            NEntry.undraw()
                            Ptext.undraw()
                            PEntry.undraw()
                            Lbutton.undraw()
                            LText.undraw()
                            SName.undraw()
                            Inventory()
                        else:
                            W = Text(Point(4,5.5), 'The Password or username you entered is Wrong ')
                            W.setFill('yellow')
                            W.setSize(20)
                            W.draw(win)
                            time.sleep(2)
                            W.setText('Enter a correct Username and Password')
                            time.sleep(2)
                            W.setText('')
                            LogIn()
                    elif 7.8<=w.getX()<=9 and 2<=w.getY()<=2.4:
                            win.close()
                    else:
                        W = Text(Point(4,5.5), 'Click the LogIn or exit button')
                        W.setFill('yellow')
                        W.setSize(25)
                        W.draw(win)
                        time.sleep(2)
                        W.setText('')
                        LogIn()
                LogIn()
            haha()
        except SyntaxError:
            Sn = Text(Point(4,5.5), 'Username or password is empty')
            Sn.setSize(25)
            Sn.setFill('yellow')
            Sn.draw(win)
            time.sleep(2)
            Sn.setText('')
            LogIn()

        except GraphicsError:
            try:
                win.close()
            except GraphicsError:
                win.close()
x=start()
x.main()
time.sleep(2)

