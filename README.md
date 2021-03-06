## Welcome to the EetlessBot 

<center style="border:3px; border-style:solid; border-color:#FF0000; padding: 1em;”text-align: center; ”font-size: 125%;”">
This site is still in progress!
</center>

The EetlessBot is a handy helper that reads text messages from the 'eetless' Telegram group of the ATLAS student house in Delft. By using specific commands, meals can be scheduled and balanced. In the future the bot will be able to enter the calculated costs for each participating member into an accounting app like splitser. 

### Commands

The bot is able to process the common commands that have been traditionally used in the chat. 

<blockquote>
<code> K:</code>  I am cooking and invite people to join my meal.<br>
<code>E:</code>  I would like to eat or join an announced meal.<br>
<code>+N:</code>  N friends are added to your balance.<br>
<code>-N:</code>  N firends are removed from your balance. Only works if you have added them before.<br>
<code>X:</code>  I do no longer want to participate in the given meal.<br>
<code>Si:</code>  Closes the inquiry to join the meal (Can only be used by the person cooking.)<br>
<code>first_name:</code>  A person who is not yourself, bu lives in the house is added to the meal. Please always use the first name that the person uses on Telegram. If you want to add friends who do not live in the house, please use the +N command. <br>
</blockquote>

Furthermore, there are a few helper commands to make life a little easier.
<blockquote>
<code>/help</code>: Prints a brief overview of the bots functionalities and commands in the chat.
/status: Prints a current overview of the scheduled meal.<br>
<code>/howmany:</code>  Returns the current number of participants for the ongoing meal.<br>
<code>/price XX.XX:</code> Registers XX.XX Euro as payed by the person sending this command and splits the costs accordingliy among the participants.<br>
</blockquote>
