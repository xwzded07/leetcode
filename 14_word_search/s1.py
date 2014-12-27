#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if not board or not board[0]:
            return False
        if not word:
            return True
        self.board = board
        self.word = word
        self.w = len(board[0])
        self.h = len(board)
        self.used = [[False for col in xrange(0, self.w)] for row in xrange(0, self.h)]

        for row in xrange(0, self.h):
            for col in xrange(0, self.w):
                if self.board[row][col] == word[0]:
                    for i in xrange(0, self.h):
                        for j in xrange(0, self.w):
                            self.used[i][j] = False
                    if self.dfs(0, row, col):
                        return True
        return False

    def in_board(self, row, col):
        return True if row >= 0 and row < self.h and col >= 0 and col < self.w else False

    def dfs(self, ci, row, col):
        if ci == len(self.word):
            return True

        if self.in_board(row, col) and not self.used[row][col] and  self.board[row][col] == self.word[ci]:
            self.used[row][col] = True
            if self.dfs(ci + 1, row, col + 1):
                return True
            if self.dfs(ci + 1, row, col - 1):
                return True
            if self.dfs(ci + 1, row + 1, col):
                return True
            if self.dfs(ci + 1, row - 1, col):
                return True
            self.used[row][col] = False
        else:
            return False


board = [
  "ABCE",
  "SFCS",
  "ADEE"
]
s = Solution()
print s.exist(board, "ABCCED") # True
print s.exist(board, "SEE") # True
print s.exist(board, "ABCB") # False
print s.exist(["aa"], "aa") # True
print s.exist(["pfhnuvuzzpujstpivosmqlctynsputylyiaufutfjnqdjfnevftotvhticjevjrvrrpxl","kewzubibppwwikpdulnwusrdjoxbdwopalowoxxdotcwgrzaeowygpesddvizjzbwnxlm","uqanswtmxvqorruixonajvbvuctkzgwtxzirxedxzwltphbmwpmhmncjpwvqctjbsttsx","ypxwcqljtxfklpxarirpdhuwsxpmqjjryinaabluytekidkblerolnnekeqdnbulkjnkk","ygltlxbqhdclwszjfftjvwwysjkeyxqxdbqqyuhixlvvduelbzwwytxqehwdenckquarq","jznuwiatonuojtmeqejzbogqsqimszdcysyvdaqrnkhxdtdtyovbcbtwrbjlbonbioynq","ohezodciiyixvlbweypfjagxqihegvuvcawsfacoyklvvmrbkghthnsxxcdexzbbcxthx","wxyiitgxnhjtqfcgxbdbejygmbilxrjvpjfzelwtvinlnrtmtxoziofvqngnfrkwcpvhd","scycplpjhbcepbmehhwwqldhvzkkvtnpvnrnbgwijyozbcfkmbhcmkjjmvthojykyrzbx","vjivzjycojorqqfcbooxixltvxrowtntewqefpgwywnqotuphjmriakgzcuyxitbekflz","nhzjvpzqlpxwdpffbnfdhfarycxijjjzqiknzkdlzdhesoktbpzlubcufadrloqbzarak","unlxxqrlanproanpehvemmpbetcekcrgqegnwxaympparcqwmnaybsbfndlxgcfwjllfj","levdvwuyoqmbtkclmjaruxxxeviqinbutwxpurpkkdndnrqbaqtvpsutqcjyrksnjrefl","vsvyfanxspxikuzeouusgtmqnzbffjqabnygpnfhcfrozqtokniqiujwvmbavtayiahxo","mesrvjrnchxrrqambwjnzklsmjcpszfffxycgrrkaqesgeghcpvbbivqrxfmykrfjrhsj","aejqidxmjgqbbreloufnzrllisxbbpkbtwscbpqnvhozaskpnpcoiqcqizskoeljcfleu","crslhtlbfaqxfffvhyfgsrwwffbktfhxybifutgbwxybeeyleftwxrucyvorcvoayyfss","ouqlutparcewxcvqxxouogxjwxivfcptyfgvyxvrbcpyelobkeyykvkjuuezytuxaauax","ptytiyytobetzefuoopksqjnlipncpntilntmlocmuvozdiprzamsjbfrrstifmttbmfm","ahbxfpwizlbblptwrynkqisyxnrybynehobodxyekafypyuiykspsnpragqegdintleyi","ccucisuinchxvyrinjktzobeyqxjuvtxxobhgvqvyxuvxmfkvpfwggaewzotuhqtxrben","tbnswkpipzfggbmmdtkchdwqtrqnuwcnxphtzwdqxiwdjjrmccolfmdbgtqapsqpjxikw","matuwzghqslujycvefbzvernugyrqinekjziihsazdviexgicjjznaohimzzwodgxeqhl","iknofvsedcinnjaoxkyjlxfbdnbjdixoskczhwflapanycdvmcgzblbgacqgknufxyggu","orudrjcunzirgiutjbultcxgwefullqzfmewvgskgbdojyhuzdfsfeabjfxuspvxbzwzi","olqrpecnnwordgwiiarpznhpkhsldtvtfnlurnjhmxypfuznwscwhlnrshfvbapiocchp","nodmovrlughnifutsooatjdvallcptucjzoyuhjpnsexyyssogujsxfuiqxxltbxsrxny","ienaimaihtxnnghllcvebvrwwooqldqtjewrswazrzpffwstapxbkqxjfozstpodvkwog","ypaxefddzydoxhbngkuwjnqybvwlrktsbtpgaulbsqqpxrdedxammsmnniahuwbwpqesl","rtdhlvfealhzlvmgibvscenyflpwphjgdonojuvlfcltyxziyuaczpagaqcrzlzccptlj","oxpskkshjahfbkgsmntcrkcfkghzzukntzgdlymwzwccikwuzpxrabwmhflhzxwvxcykd","nhejjirvelvukmwnkivrvessanrfocibjmkuudpyomsbyookyldtrwmujfzxhjysvkopn","epeskftavdzjhsafgwomvoveoobzesmiisdsxwuvzteiognudeiysgfgwghabwljoodmk","zhjtnuhtjdwnoxhucqqkxqntbwkpbwzbflwuhfnqikgwjpqnfgxfzlaajksnitqpeojnt","xgbjmaubqhjzeqyrqadbusloibuwkirjosucsoflvokcektxmyahqlvamryzbpkpiftcv","znrpzvwjqtypvfhgcivtgwxwgogniijjwcyxxwhprhemmmtquqlcmiysxeifprqnvokun","rjeyormcmeyeqaqabkxhsewlujgluaynkeoavcejhcnzedzhqxpidnwazcltflirpyrnb","xwkzmjfrknhjesnropqqalvnuoeufrxcqhdcsltdybmctbvjqmzsxxhtlmqtdnxvxdxro","tuowjsrmnafzzxzyhumtmhyaguzltqzmnpiwhzkvzpwbpxbwunrgwpidjhodyqrlfajpz","vkbliecgfaavririrwuynzyfqjmqubsqlvdwzhcgjebcmvkdtgegfclyoaqibkapfflgo","nnxtobflmjfunlarzyfzqqcbsrgacnoraokqpqcdbhyquahvanwqfzrxsaxvnoopczhrr","lxsuvkpxrmxglpnkhlchkzwyonanuuggraaokrndgkkrzxbikfrvfnvvaykxuqdnqfbaz","odfapybpbmbgdynruktsuqmkvzcdcecskjubhxqkjusnsigmszgnqsznteqxispsdlumj","mwsgphzxnnrpugfogsikjhudznhkjvtvsocjvdglqzakghzmzjykqsqrhzcquxmmlqvjt","dujduwjbvxcgxpyrfqzgspardpdtkooqiyteuehrdlzaaxrhnqnhiqbnfgjruxhexciti","rmlcllfjfmyxcihujvzpeqjbanbcxulojysumxfrmeoqmwkvtjmxbvabkdgjatzjrrddp","jwbnnrblbyemkbphdtthzchubqnsvrjepktcdwngwruiukpadkheoqypilkdetkugdylc","muyfohcyycbjlhxbfpjtbmxuytccsqggkenynpzmtaxeiufplqimfgjdbnhtdnbpupohg","nvapsezpmraeznjhypjlwermiggzwpfllhbdmcsatvevkqcifnvdumpcvxbrnifyqgdek","ygetmzfcdnjrknnzcpwcsnpaupscswnsetlruqtxfdqssdrwunymcppxehzzgorkhfbbv","xbdarxuvoqpdrehgtglaimiwdteiuhgriltaipxygodzukfntsqbeyxktdsqnahvldxts","wtalwzhjhvczndgncqjgizvjiqwlosgmlixkkhtrevsraygcopkzqfkzyimmasymdywnh","relmweoxkqncdmskytihgwhaxvdxtqekwpyvvosfhfjkueuuxfbdbleaijxeadqyuptpd","nvmvgwpktlkapnbctekdbofhfdbwzrbmoohumyhhkrhzgldapnfsekzlpbjoumdickepl","lwxeeylrbngqsaucahtdqixdlhfxlwkxvhbbfosibaztavxadrfvbeymlglxewuzfxcnm","uvpuwjxsixvzfqajrovzcsfyohfnjsbgqrcmazeixbkesmnldimfcrfsykgifhovyshas","mlrpvvjjiumtirxayqajwiofylersgjgrawoxfyfckakeymcqnnoxdtwozpjgapxcnmzt","mgxwjhcjufzjsngyicmitvqvnnzabavnjsmscobytchopnoxschnyxjnnknqlleudsmhg","pfcrosicghwipjiouvbfluqwykbsylynsaghuolavhlmqtbnreseyicyufquqrjjtpsof","doakbpcvqpowjuxtwvpbojufudyjvmqadtkeiobagrwpltlhralhkfmgkmqhzihebtkjj","ojrfihtduawundgupneefndnwjpptabhmspubizvkwsybystnzxsocillzcezdonwdjzl","jvvhnvknqdbpavdefopgrwiwmvspfscqpzzevjrlnucpsfuxwjephmltjgkoamgpmftjp","muchwtzdnybzeqgsecckmskzzbneuwvgszpototipvhtnqorsqdekpdlqsqkontgniwgz","sqonyjcozwipzmcpsnhkfsztnhiveqwwgmleypuxlepnrrelenvmfwfugnskdoijbvqbm","myarnpkgtvngszopgkvtchyrrjuobxaovahlprrkoetgfjxltugwdgpwqlktilhflqqdj","knxoggwpfhlcojfuycmlogvzpangtqrdfrtoxpfexqgnzmjzqwkeehgtivbbnvgsmzglp","opoewbgkkfaisgobokjjnmwisruuxfjnvxutaadmhfxbnldcvonjdkrxboravcosbilbk","qqrvnvjyynuoafrmwppmgqijgakqooceevcrqnrqalfcswppnedwwlfeorwefyilukckx","udzhicagtrwzusyixeyqbcybmjvzoiyilarvetdxkzyhryrqdrjgvhhhqdienjoajixnb","ammckvvjmmodxuyebhwgsbtbrvkzszdtlpxxmsiagwfdsdjumgcejyhattcosfjfwgdiy","nkhmpkeuuagafnjdwlyqnmiuvqqdtacikjubvbvrberirclnqmffyoaweszzvdjhoejmh","edikxtbzerrswxtmzpsrqtowdwmjhyqncaybtbcauustrnhsealxvatayhlhgdukeslzw","nbqjwjcjruotglqigrinepvijhoeunairstncwyvsoqabgihzsxehuotccxwrzgiraxvy","yqqmgropbxouuubpiwrktpcuwmmykjwiaowifkxjiodeigtrdmbycftashyeqwoskkdsv","abfogjzmfqprrovzjxrqvvitjbgveysgbxxhjwtomlhfbdekaxcysktdnzbrztaarxhcv","dqjqxorcvddshdnrwsfwtyxnaygxhiumydcxstapyfhfiwzgpgcigaxhadghnbwneylyu","nnssxactzikfntnpsupwbylcuzivmhpzwjttjvpkfzrsufhnzylczwetxpojwfkupfoaa","fliecazhkojizlhvsdvjtefzrbqwrqzwbhbghcptqacrmjogojpiqwjhxzdppentlozvs","qokrsbfcqlsbcarajyzieoaietwsurnkhxdabietvwuzzmzimztqptbtoxoiqduxcazdi","dygctfbhhjtgemxxntnkjxcmsbqsbucguiinqjuxvqfzcczrxmdikfuegnyhhcqblyrdk"], "afdfghjhy")
