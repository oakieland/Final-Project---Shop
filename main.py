import sys
from PyQt6.QtWidgets import *
from gui import *


class shop(QMainWindow, Ui_MainWindow):
    COIN_VALUES = {
        'platinum': 1000,
        'gold': 100,
        'electrum': 50,
        'silver': 10,
        'copper': 1
    }

    CP = COIN_VALUES["copper"]
    SP = COIN_VALUES["silver"]
    EP = COIN_VALUES["electrum"]
    GP = COIN_VALUES["gold"]
    PP = COIN_VALUES["platinum"]

    def __init__(self):
        """
        Method to Initialize GUI interface
        """
        super().__init__()
        self.setupUi(self)

        self.player_wallet = {
            'platinum': 0,
            'gold': 0,
            'electrum': 0,
            'silver': 0,
            'copper': 0
        }

        self.total_wallet = 0
        self.total_cost = 0

        self.submit_wallet.clicked.connect(lambda: self.fund_wallet())
        self.submit_shop.clicked.connect(lambda: self.shopping())
        self.submit_purchase.clicked.connect(lambda: self.purchase())

    def fund_wallet(self):
        pp = self.player_pp.value()
        gp = self.player_gp.value()
        ep = self.player_ep.value()
        sp = self.player_sp.value()
        cp = self.player_cp.value()

        wallet = self.player_wallet

        if pp > 0 or 0 > pp:
            wallet["platinum"] += pp
            self.total_wallet += pp * shop.PP
            self.amount_pp.setText(str(wallet["platinum"]))
            if pp <= 0:
                wallet["platinum"] = 0
                self.amount_pp.setText(str(wallet["platinum"]))
            self.player_pp.setValue(0)

        if gp > 0 or 0 > gp:
            wallet["gold"] += gp
            self.total_wallet += gp * shop.GP
            self.amount_gp.setText(str(wallet["gold"]))
            if gp < 0:
                wallet["gold"] = 0
                self.amount_gp.setText(str(wallet["gold"]))
            self.player_gp.setValue(0)

        if ep > 0 or 0 > ep:
            wallet["electrum"] += ep
            self.total_wallet += ep * shop.EP
            self.amount_ep.setText(str(wallet["electrum"]))
            if ep < 0:
                wallet["electrum"] = 0
                self.amount_ep.setText(str(wallet["electrum"]))
            self.player_ep.setValue(0)

        if sp > 0 or 0 > sp:
            wallet["silver"] += sp
            self.total_wallet += sp * shop.SP
            self.amount_sp.setText(str(wallet["silver"]))
            if sp < 0:
                wallet["silver"] = 0
                self.amount_sp.setText(str(wallet["silver"]))
            self.player_sp.setValue(0)

        if cp > 0 or 0 > cp:
            wallet["copper"] += cp
            self.total_wallet += cp * shop.CP
            self.amount_cp.setText(str(wallet["copper"]))
            if cp < 0:
                wallet["copper"] = 0
                self.amount_cp.setText(str(wallet["copper"]))
            self.player_cp.setValue(0)

        if self.total_wallet < 0:
            self.total_wallet = 0

    def shopping(self):
        ration = self.amount_ration.value() * shop.EP
        material = self.amount_material.value() * shop.EP
        simple_weap = self.amount_simple.value() * (shop.GP * 2)
        martial_weap = self.amount_martial.value() * (shop.GP * 5)
        light_armor = self.amount_light.value() * shop.PP
        medium_armor = self.amount_medium.value() * (shop.PP * 5)
        magic_item = self.amount_magic.value() * (shop.PP * 5)
        formula = self.amount_formula.value() * (shop.PP * 10)
        upgrade = self.amount_upgrade.value() * (shop.GP * 15)

        if ration > 0 or 0 > ration:
            self.total_cost += ration
            if ration < 0:
                self.total_cost -= ration

        if material > 0 or 0 > material:
            self.total_cost += material
            if material < 0:
                self.total_cost -= material

        if simple_weap > 0 or 0 > simple_weap:
            self.total_cost += simple_weap
            if simple_weap < 0:
                self.total_cost -= simple_weap

        if martial_weap > 0 or 0 > martial_weap:
            self.total_cost += martial_weap
            if martial_weap < 0:
                self.total_cost -= martial_weap

        if light_armor > 0 or 0 > light_armor:
            self.total_cost += light_armor
            if light_armor < 0:
                self.total_cost -= light_armor

        if medium_armor > 0 or 0 > medium_armor:
            self.total_cost += medium_armor
            if medium_armor < 0:
                self.total_cost -= medium_armor

        if magic_item > 0 or 0 > magic_item:
            self.total_cost += magic_item
            if magic_item < 0:
                self.total_cost -= magic_item

        if formula > 0 or 0 > formula:
            self.total_cost += formula
            if formula < 0:
                self.total_cost -= formula

        if upgrade > 0 or 0 > upgrade:
            self.total_cost += upgrade
            if upgrade < 0:
                self.total_cost -= upgrade

        self.total_cost = (ration + material + simple_weap + martial_weap + light_armor +
                           medium_armor + magic_item + formula + upgrade)

        final_coinage = {
            'platinum': 0,
            'gold': 0,
            'electrum': 0,
            'silver': 0,
            'copper': 0,
        }

        for coin in final_coinage:
            final_coinage[coin] = self.total_cost // self.COIN_VALUES[coin]
            self.total_cost %= self.COIN_VALUES[coin]

        self.result.setText(
            f"PP {final_coinage['platinum']}<br>GP {final_coinage['gold']}<br>EP {final_coinage['electrum']}<br> SP {final_coinage['silver']}<br> CP {final_coinage['copper']}")

        self.total_cost = (ration + material + simple_weap + martial_weap + light_armor +
                           medium_armor + magic_item + formula + upgrade)

    def purchase(self):

        if self.total_wallet >= self.total_cost:
            self.cost.setText("Purchase, Successful")
            self.result.setStyleSheet("background-color: rgb(0, 255, 128);")
            self.total_wallet -= self.total_cost
            save_wallet = self.total_wallet

            for coin in self.player_wallet:
                self.player_wallet[coin] = self.total_wallet // self.COIN_VALUES[coin]
                self.total_wallet %= self.COIN_VALUES[coin]

            self.amount_pp.setText(str(self.player_wallet["platinum"]))
            self.amount_gp.setText(str(self.player_wallet["gold"]))
            self.amount_ep.setText(str(self.player_wallet["electrum"]))
            self.amount_sp.setText(str(self.player_wallet["silver"]))
            self.amount_cp.setText(str(self.player_wallet["copper"]))

            self.total_wallet = save_wallet
            print(self.total_wallet)



        elif self.total_wallet < self.total_cost:
            self.cost.setText("Purchase, Failed - Not Enough Funds")
            self.result.setStyleSheet("background-color: rgb(255, 161, 161);")

        else:
            self.result.setStyleSheet("background-color: rgba(0, 0, 0, 0);")


def main():
    application = QApplication([])
    window = shop()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
