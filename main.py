import sys
from PyQt6.QtWidgets import *
from gui import *


class shop(QMainWindow, Ui_MainWindow):
    # Coins are broken down into their Copper Value.
    COIN_VALUES = {
        'platinum': 1000,
        'gold': 100,
        'electrum': 50,
        'silver': 10,
        'copper': 1
    }

    # Creates a shortcut so I don't have to rewrite this.
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

        # user starts off with no money.
        self.player_wallet = {
            'platinum': 0,
            'gold': 0,
            'electrum': 0,
            'silver': 0,
            'copper': 0
        }

        # Total Wallet is the total amount of money if the coins are broken down.
        self.total_wallet = 0

        # Total Cost is the total amount of money the user is charged.
        self.total_cost = 0

        # Initializing buttons
        self.submit_wallet.clicked.connect(lambda: self.fund_wallet())
        self.submit_shop.clicked.connect(lambda: self.shopping())
        self.submit_purchase.clicked.connect(lambda: self.purchase())

    def fund_wallet(self) -> None:
        """
        Updates the GUI and breaks down the money the player has when the submit
        button is pressed.
        :return: None
        """
        # Shorthand the coin values.
        pp = self.player_pp.value()
        gp = self.player_gp.value()
        ep = self.player_ep.value()
        sp = self.player_sp.value()
        cp = self.player_cp.value()
        wallet = self.player_wallet

        # Check the amount of platinum the character is adding or subtracting.
        if pp > 0 or 0 > pp:
            wallet["platinum"] += pp
            self.total_wallet += pp * shop.PP
            self.amount_pp.setText(str(wallet["platinum"]))

            # Make sure the character's platinum doesn't go below 0. No debt.
            if pp <= 0:
                wallet["platinum"] = 0
                self.amount_pp.setText(str(wallet["platinum"]))
            self.player_pp.setValue(0)

        # Check the amount of gold the character is adding or subtracting.
        if gp > 0 or 0 > gp:
            wallet["gold"] += gp
            self.total_wallet += gp * shop.GP
            self.amount_gp.setText(str(wallet["gold"]))

            # Make sure the character's gold doesn't go below 0. No debt.
            if gp < 0:
                wallet["gold"] = 0
                self.amount_gp.setText(str(wallet["gold"]))
            self.player_gp.setValue(0)

        # Check the amount of electrum the character is adding or subtracting.
        if ep > 0 or 0 > ep:
            wallet["electrum"] += ep
            self.total_wallet += ep * shop.EP
            self.amount_ep.setText(str(wallet["electrum"]))

            # Make sure the character's electrum doesn't go below 0. No debt.
            if ep < 0:
                wallet["electrum"] = 0
                self.amount_ep.setText(str(wallet["electrum"]))
            self.player_ep.setValue(0)

        # Check the amount of silver the character is adding or subtracting.
        if sp > 0 or 0 > sp:
            wallet["silver"] += sp
            self.total_wallet += sp * shop.SP
            self.amount_sp.setText(str(wallet["silver"]))

            # Make sure the character's silver doesn't go below 0. No debt.
            if sp < 0:
                wallet["silver"] = 0
                self.amount_sp.setText(str(wallet["silver"]))
            self.player_sp.setValue(0)

        # Check the amount of copper the character is adding or subtracting.
        if cp > 0 or 0 > cp:
            wallet["copper"] += cp
            self.total_wallet += cp * shop.CP
            self.amount_cp.setText(str(wallet["copper"]))

            # Make sure the character's copper doesn't go below 0. No debt.
            if cp < 0:
                wallet["copper"] = 0
                self.amount_cp.setText(str(wallet["copper"]))
            self.player_cp.setValue(0)

        # Make sure the character's total wallet amount is not in the negatives.
        if self.total_wallet < 0:
            self.total_wallet = 0

    def shopping(self) -> None:
        """
        Allows the user to pick and choose what items they wish to have.
        Generates a receipt.
        :return: None
        """

        # Makes each shop item worth their value
        ration = self.amount_ration.value() * shop.EP
        material = self.amount_material.value() * shop.EP
        simple_weap = self.amount_simple.value() * (shop.GP * 2)
        martial_weap = self.amount_martial.value() * (shop.GP * 5)
        light_armor = self.amount_light.value() * shop.PP
        medium_armor = self.amount_medium.value() * (shop.PP * 5)
        magic_item = self.amount_magic.value() * (shop.PP * 5)
        formula = self.amount_formula.value() * (shop.PP * 10)
        upgrade = self.amount_upgrade.value() * (shop.GP * 15)

        # Makes sure the item's price is added to the cost. Make sure if the item is removed it isn't added to the cost.
        if ration > 0 or 0 > ration:
            self.total_cost += ration
            if ration < 0:
                self.total_cost -= ration

        # Makes sure the item's price is added to the cost. Make sure if the item is removed it isn't added to the cost.
        if material > 0 or 0 > material:
            self.total_cost += material
            if material < 0:
                self.total_cost -= material

        # Makes sure the item's price is added to the cost. Make sure if the item is removed it isn't added to the cost.
        if simple_weap > 0 or 0 > simple_weap:
            self.total_cost += simple_weap
            if simple_weap < 0:
                self.total_cost -= simple_weap

        # Makes sure the item's price is added to the cost. Make sure if the item is removed it isn't added to the cost.
        if martial_weap > 0 or 0 > martial_weap:
            self.total_cost += martial_weap
            if martial_weap < 0:
                self.total_cost -= martial_weap

        # Makes sure the item's price is added to the cost. Make sure if the item is removed it isn't added to the cost.
        if light_armor > 0 or 0 > light_armor:
            self.total_cost += light_armor
            if light_armor < 0:
                self.total_cost -= light_armor

        # Makes sure the item's price is added to the cost. Make sure if the item is removed it isn't added to the cost.
        if medium_armor > 0 or 0 > medium_armor:
            self.total_cost += medium_armor
            if medium_armor < 0:
                self.total_cost -= medium_armor

        # Makes sure the item's price is added to the cost. Make sure if the item is removed it isn't added to the cost.
        if magic_item > 0 or 0 > magic_item:
            self.total_cost += magic_item
            if magic_item < 0:
                self.total_cost -= magic_item

        # Makes sure the item's price is added to the cost. Make sure if the item is removed it isn't added to the cost.
        if formula > 0 or 0 > formula:
            self.total_cost += formula
            if formula < 0:
                self.total_cost -= formula

        # Makes sure the item's price is added to the cost. Make sure if the item is removed it isn't added to the cost.
        if upgrade > 0 or 0 > upgrade:
            self.total_cost += upgrade
            if upgrade < 0:
                self.total_cost -= upgrade

        # Total cost is all the items added together.
        self.total_cost = (ration + material + simple_weap + martial_weap + light_armor +
                           medium_armor + magic_item + formula + upgrade)

        # Copy of potential coins
        final_coinage = {
            'platinum': 0,
            'gold': 0,
            'electrum': 0,
            'silver': 0,
            'copper': 0,
        }

        # Break down the costs into coins
        for coin in final_coinage:
            final_coinage[coin] = self.total_cost // self.COIN_VALUES[coin]
            self.total_cost %= self.COIN_VALUES[coin]

        # Update GUI with final result.
        self.result.setText(
            f"PP {final_coinage['platinum']}<br>GP {final_coinage['gold']}<br>EP {final_coinage['electrum']}<br> SP {final_coinage['silver']}<br> CP {final_coinage['copper']}")

        # Make sure the total cost keeps its integrity.
        self.total_cost = (ration + material + simple_weap + martial_weap + light_armor +
                           medium_armor + magic_item + formula + upgrade)

    def purchase(self) -> None:
        """
        Updates the GUI to be green if the purchase is successful.
        Breaks down the amount of money the character has returned.
        Updates the GUI to be red if the purchase was a failure.
        Otherwise, don't update the gui
        :return: None
        """

        # Purchase was successful, turn the background green and update the wallet.
        if self.total_wallet > self.total_cost:
            self.cost.setText("Purchase, Successful")
            self.result.setStyleSheet("background-color: rgb(0, 255, 128);")
            self.total_wallet -= self.total_cost
            save_wallet = self.total_wallet

            # Break down the new wallet into coins
            for coin in self.player_wallet:
                self.player_wallet[coin] = self.total_wallet // self.COIN_VALUES[coin]
                self.total_wallet %= self.COIN_VALUES[coin]

            # Update GUI for the user's coins.
            self.amount_pp.setText(str(self.player_wallet["platinum"]))
            self.amount_gp.setText(str(self.player_wallet["gold"]))
            self.amount_ep.setText(str(self.player_wallet["electrum"]))
            self.amount_sp.setText(str(self.player_wallet["silver"]))
            self.amount_cp.setText(str(self.player_wallet["copper"]))

            # Keep the wallet total's integrity.
            self.total_wallet = save_wallet

        # Turn red if the user cannot afford wares.
        elif self.total_wallet < self.total_cost:
            self.cost.setText("Purchase, Failed - Not Enough Funds")
            self.result.setStyleSheet("background-color: rgb(255, 161, 161);")

        # Update the GUI if neither of the previous if statements function
        else:
            self.cost.setText("Total Cost")
            self.result.setStyleSheet("background-color: rgba(0, 0, 0, 0);")


def main():
    application = QApplication([])
    window = shop()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
