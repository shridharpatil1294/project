{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b28d2b77",
   "metadata": {},
   "outputs": [],
   "source": [
    "admin_keys = {\"Shridhar\": \"Shridhar@9673\"}\n",
    "\n",
    "menu = {1: {'Food Name': 'Butter Chicken', 'Food ID': 1, 'Price': 950, 'Discount': 4, 'Stock': 14},\n",
    "        2: {'Food Name': 'Roti', 'Food ID': 2, 'Price': 10, 'Discount': 0, 'Stock': 123},\n",
    "        3: {'Food Name': 'Cake', 'Food ID': 3, 'Price': 1070, 'Discount': 7, 'Stock': 5}}\n",
    "\n",
    "\n",
    "def add_new_item():\n",
    "    foodname = input(\"Enter the foood name: \")\n",
    "    foodid = int(input(\"Enter the food id: \"))\n",
    "    price = int(input(\"Enter the price of the food: \"))\n",
    "    discount = int(input(\"Enter the discount of food: \"))\n",
    "    stock = int(input(\"Enter te stock value of food: \"))\n",
    "    menu[foodid] = {\n",
    "        \"Food Name\": foodname,\n",
    "        \"Food ID\": foodid,\n",
    "        \"Price\": price,\n",
    "        \"Discount\": discount,\n",
    "        \"Stock\": stock\n",
    "    }\n",
    "    print(f\"The {foodname} is successfully added\")\n",
    "    return menu\n",
    "\n",
    "\n",
    "def edit_from_item():\n",
    "    food = int(input(\"Enter the foodid which you want to edit: \"))\n",
    "    a = input(\"Enter the food name\")\n",
    "    b = int(input(\"Enter the price of food\"))\n",
    "    c = int(input(\"Enter the discount of food\"))\n",
    "    d = int(input(\"Enter the stock of the food\"))\n",
    "    menu[food][\"Food Name\"] = a\n",
    "    menu[food][\"Price\"] = b\n",
    "    menu[food][\"Discount\"] = c\n",
    "    menu[food][\"Stock\"] = d\n",
    "    print(\"*****Edit food item successfully*****\")\n",
    "    return menu\n",
    "\n",
    "def show_menu():\n",
    "    print(\"*****HERE IS THE MENU OF SHRIDHAR'S DHABA*****\")\n",
    "    for i in menu:\n",
    "        print(\"Food Name: \",menu[i][\"Food Name\"])\n",
    "        print(\"Price: \",menu[i][\"Price\"],\"INR\")\n",
    "        print(\"Food ID: \",menu[i][\"Food ID\"])\n",
    "\n",
    "def remove_food_item():\n",
    "    d = int(input(\"Enter the food id which you want to exit\"))\n",
    "    menu.pop(d)\n",
    "    print(\"Remove food item successfully \")\n",
    "    return "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7458f9a9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
