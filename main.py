{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "296ed50d",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_8544/1509589870.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0madmin\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0maa\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0muser\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mUser\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0muhh\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mUser\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\admin.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     61\u001b[0m   {\n\u001b[0;32m     62\u001b[0m    \u001b[1;34m\"cell_type\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"code\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 63\u001b[1;33m    \u001b[1;34m\"execution_count\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     64\u001b[0m    \u001b[1;34m\"id\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"7458f9a9\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     65\u001b[0m    \u001b[1;34m\"metadata\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import admin as aa\n",
    "from user import User\n",
    "\n",
    "uhh = User(str, str, str, str, str)\n",
    "\n",
    "inp = int(input(\"Where You want to login select 1.Admin and 2.User 0.Exit\"))\n",
    "if inp == 1:\n",
    "    Username = input(\"Enter the username of admin: \")\n",
    "    Password = input(\"Enter the password of admin: \")\n",
    "    if aa.admin_keys[Username] == Password:\n",
    "        print(\"*****You're successfully logged inn*****\")\n",
    "        admin_crawler = True\n",
    "        while admin_crawler:\n",
    "            adm_choice = int(input(\"Choose the options of admin panel 1.ADD NEW FOOD 2.EDIT FOOD ITEM 3.VIEW MENU 4.REMOVE FOOD ITEM 5.EXIT\"))\n",
    "            if adm_choice == 1:\n",
    "                aa.add_new_item()\n",
    "            elif adm_choice == 2:\n",
    "                aa.edit_from_item()\n",
    "            elif adm_choice == 3:\n",
    "                aa.show_menu()\n",
    "            elif adm_choice == 4:\n",
    "                aa.remove_food_item()\n",
    "            elif adm_choice == 5:\n",
    "                print(f\"You're Exit to the admin panel{Username}\")\n",
    "                admin_crawler = False\n",
    "            else:\n",
    "                print(\"This is the wrong selection please select valid option\")\n",
    "    else:\n",
    "        print(\"These are the wrong credentials! SORRY!!!\")\n",
    "elif inp == 2:\n",
    "    print(\"Welcome to the user panel\")\n",
    "    username = input(\"Enter the username here: \")\n",
    "    password = input(\"Enter the password here: \")\n",
    "    if User.login(username, password):\n",
    "        print(f\"You are logged in successfully {username}\")\n",
    "        user_crawler = True\n",
    "        while user_crawler:\n",
    "            usr_choice = int(input(f\"{username}, Enter the option 1.Place new order 2.Update Profile 3.Order history 4.See profile 5.Exit\"))\n",
    "            if usr_choice == 1:\n",
    "                uhh.place_order()\n",
    "            elif usr_choice == 2:\n",
    "                uhh.update_profile()\n",
    "            elif usr_choice == 3:\n",
    "                print(f\"Here is your order history, {username}\")\n",
    "                print(uhh.order_history)\n",
    "            elif usr_choice == 4:\n",
    "                uhh.watch_profile()\n",
    "            elif usr_choice == 5:\n",
    "                user_crawler = False\n",
    "                print(\"You're Successfully looged out\")\n",
    "            else:\n",
    "                print(\"You choose the invalid option\")\n",
    "    else:\n",
    "        print(\"These are the wrong credentials! SORRY!!!\")\n",
    "else:\n",
    "    print(\"You selected the wrong or invalid option\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b0b8d08",
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
