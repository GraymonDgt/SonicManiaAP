#include "APCpp/Archipelago.h"
#include "ManiaAP.h"


int recievedItems[150];


void onItemClear()
{
    for (int i = 0; i < 150; i++) {
        recievedItems[i]= 0;
    }
    }

void onItemReceived(int itemId, bool notify) { 
    recievedItems[itemId] += 1;
}

void onLocationChecked(int locationId)
{
    // Mark the location as checked in your game.
}

void ManiaAP_Init(const char *server, const char *game, const char *slot, const char *password){

	AP_Init(server, game, slot, password);



    AP_SetItemClearCallback(onItemClear);
    AP_SetItemRecvCallback(onItemReceived);
    AP_SetLocationCheckedCallback(onLocationChecked);
    for (int i = 0; i < 150; i++) {
        recievedItems[i] = 0;
    }
    AP_Start();

    }

void ManiaAP_SendItem(int item){
	
	
	AP_SendItem(item);
	
}
void ManiaAP_Goal(void){
	AP_StoryComplete();
}
int ManiaAP_hasItem(int id) {

    return recievedItems[id]; }

