# State migration proposal euler-5 -> euler-6

Here is a proposal of agents state migration between euler-5 -> euler-6. There are 4 major things should be taken into account:

- cyberlinks by agent
- karma by agent
- precommits by validator
- stake by validator

Given the circumstances karma by agent unit compromised by the [bug](https://github.com/cybercongress/cyberd/issues/460) so there is no sense to migrate karma values clearly between testnets. But the solution is in the cyberlinks migrations. It possible to export all cyberlinks by agent to IPLD structure and add possibility for agents to make their cyberlinks again in the new testnet by one transaction. This way it's possible to cover two migration entities: cyberlinks and karma.The weakness of that method is anyone can relink all cyberlinks before pioneers or discoverers. 


The precommits migration is complex. To avoid additional changes in distribution the proposal is to save precommits state in [`.csv` file](https://github.com/cybercongress/launch-kit/tree/0.1.0/game_rewards_calculations) on block height and use it for the Game of Links calculations after the Game. Thus, we can avoid major changes in distribution and make migration softly. 

The stake of validators should be burned. The complexity of changing distribution parameters much higher than the error of final stake results. 

In addition, we can in detail test the genesis ceremony and parameters discussion. As launch-kit repo ready for newcomers it seems possible to do that.

The workflow is pretty easy:

1. Announcement of network stop on the block height
2. Precommits and cyberlinks export on block
3. The UI for cyber.page to cyberlinks import
4. The guide for cyberlinks import by the CLI
5. Genesis generation
6. Genesis ceremony
7. Relaunch
