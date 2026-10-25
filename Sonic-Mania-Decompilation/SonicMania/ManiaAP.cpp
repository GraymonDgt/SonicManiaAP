#include "APCpp/Archipelago.h"
#include "ManiaAP.h"

#include <json/json.h>
#include <json/reader.h>
#include <json/value.h>
#include <json/writer.h>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
const int maxItems = 150;
const int maxLocs  = 300;

const std::string rlinkStr = "RingLink";
const std::string dlinkStr   = "DeathLink";
const std::string ctypeStr = "CompletionType";
const std::string bsphereStr = "SpheresLevel";

int recievedItems[maxItems];
int checkedLocations[maxLocs]; 
int spheresLevel = 0;
int goalType     = 0;
int ringlink     = 0;
int deathLink    = 0;
int queuedRings  = 0;
int sendDeath    = 0;

void onItemClear()
{
    for (int i = 0; i < maxItems; i++) {
        recievedItems[i]= 0;
    }
}

void onItemReceived(int itemId, bool notify)
{
    recievedItems[itemId] += 1;
    switch (itemId) {

        case 37:
            recievedItems[6] += 1;
            recievedItems[7] += 1;
            break;
        case 38:
            recievedItems[8] += 1;
            recievedItems[9] += 1;
            break;
        case 39:
            recievedItems[10] += 1;
            recievedItems[11] += 1;
            break;
        case 40:
            recievedItems[12] += 1;
            recievedItems[13] += 1;
            break;
        case 41:
            recievedItems[14] += 1;
            recievedItems[15] += 1;
            break;
        case 42:
            recievedItems[16] += 1;
            recievedItems[17] += 1;
            break;
        case 43:
            recievedItems[18] += 1;
            recievedItems[19] += 1;
            break;
        case 44:
            recievedItems[20] += 1;
            recievedItems[21] += 1;
            break;
        case 45:
            recievedItems[22] += 1;
            recievedItems[23] += 1;
            break;
        case 46:
            recievedItems[24] += 1;
            recievedItems[25] += 1;
            break;
        case 47:
            recievedItems[26] += 1;
            recievedItems[27] += 1;
            break;
        case 48:
            recievedItems[28] += 1;
            recievedItems[29] += 1;
            break;

        default: break;
    }
}


void onLocationChecked(int locationId)
{
    // Mark the location as checked in your game.

    checkedLocations[locationId] = 1;
}

void registerRingLink(int value) {
        ringlink = value;
        if (value > 0) {
            
            if (deathLink > 0)
            {
                AP_UpdateTags({ rlinkStr, dlinkStr });

            }
            else {
                AP_UpdateTags({ rlinkStr });
            }



        }
}


void registerDeathLink(int value)
{
    deathLink = value;
    if (value > 0) {
        if (ringlink > 0) {
            AP_UpdateTags({ rlinkStr, dlinkStr });
        }
        else {
            AP_UpdateTags({ dlinkStr });
        }
    }
}

void registerBlueSpheres(int value) { spheresLevel = value; }
void registerGoalType(int value) { goalType = value; }

void deathLinkReceived(std::string none, std::string none2) {

    sendDeath = 1; }

void bouncePacketRecieved(AP_Bounce packet) {

    Json::CharReaderBuilder builder;
    std::unique_ptr<Json::CharReader> reader(builder.newCharReader());



    Json::Value root;
    std::string errors;

    std::ofstream outFile("archipelagolog.txt", std::ios::app);

    if (outFile.is_open()) {
        outFile << errors << "\n" << packet.tags << "\n";

        outFile.close();
    }

    if (packet.tags) {
        if (std::find(packet.tags->begin(), packet.tags->end(), rlinkStr) != packet.tags->end()) {

                bool is_parsed = reader->parse(packet.data.c_str(), packet.data.c_str() + packet.data.length(), &root, &errors); 
                if (root["source"].asInt() == AP_GetPlayerID()) {
                return;
            }
        queuedRings += root["amount"].asInt();

        }
        else if (std::find(packet.tags->begin(), packet.tags->end(), dlinkStr) != packet.tags->end()) {
            sendDeath = 1;
        }
    
    
    
    
    }

}




void ManiaAP_Init(const char *server, const char *game, const char *slot, const char *password){

	AP_Init(server, game, slot, password);
    //AP_SetDeathLinkSupported(true);

    AP_RegisterSlotDataIntCallback(bsphereStr,registerBlueSpheres);

    AP_RegisterSlotDataIntCallback(dlinkStr, registerDeathLink);
        
        AP_RegisterSlotDataIntCallback(ctypeStr, registerGoalType);
    AP_RegisterSlotDataIntCallback(rlinkStr, registerRingLink);
    AP_SetDeathLinkRecvCallback(deathLinkReceived);
    AP_SetItemClearCallback(onItemClear);
    AP_SetItemRecvCallback(onItemReceived);
    AP_SetLocationCheckedCallback(onLocationChecked);
    AP_RegisterBouncedCallback(bouncePacketRecieved);
    for (int i = 0; i < maxItems; i++) {
        recievedItems[i] = 0;
    }
    for (int i = 0; i < maxLocs; i++) {
        checkedLocations[i] = 0;
    }

}



void ManiaAP_TestSendItem(int item){
	
	AP_SendItem(item);
	
}

int ManiaAP_Goal(int type){
    if (type == goalType) {
        AP_StoryComplete();
        return 1;
    }
    return 0;
	
}
int ManiaAP_hasItem(int id) {
    return recievedItems[id]; }

int ManiaAP_checkedLocation(int id) { 
    return checkedLocations[id]; }

int ManiaAP_spheresLevelDone(int level) {

    if (spheresLevel == 2) {
    
    if (checkedLocations[200 + level] > 0 && checkedLocations[232 + level] > 0) {
            return 1;
        }
        else {
            return 0;
        }
    }
    else {
        if (checkedLocations[200 + level] > 0) {
            return 1;
        }
        else {
            return 0;
        }
    }



}

int ManiaAP_collectRingQueue(void) {
    int returnRings = queuedRings;
    queuedRings = 0;
    return returnRings;
}

void ManiaAP_sendRings(int amount) {
    if (ringlink == 0 || amount == 0) {
        return;
    }
 
    AP_Bounce b;
    Json::Value v;
    std::chrono::time_point<std::chrono::system_clock> timestamp = std::chrono::system_clock::now();
    v["amount"] = amount;
    v["source"] = AP_GetPlayerID();
    v["time"] = (int64_t)std::chrono::duration_cast<std::chrono::seconds>(timestamp.time_since_epoch()).count();


    Json::StreamWriterBuilder builder;
    b.data = Json::writeString(builder, v);
    b.tags = new std::vector<std::string>(1, "RingLink");


    AP_SendBounce(b);
}

int ManiaAP_checkDeath(void) {
    if (deathLink == 0) {
        return 0;
    }
    return sendDeath;


}

void ManiaAP_sendDeath(char* reason) {
    if (deathLink == 0) {
        return;
    }
    if (sendDeath != 0) {
        sendDeath = 0;
        return;
    }
    


    std::chrono::time_point<std::chrono::system_clock> timestamp = std::chrono::system_clock::now();
    std::string reasonstr                                        = APGetPlayerName() + " " + reason;
    
    AP_Bounce b;
    Json::Value v;
    v["time"]   = (int64_t)std::chrono::duration_cast<std::chrono::seconds>(timestamp.time_since_epoch()).count();
    v["source"] = "Sonic Mania"; // Name and Shame >:D
    if (!reasonstr.empty()) {
        std::string cause_pname = reasonstr;
        constexpr std::string_view pname_you{ "%YOU%" };
        size_t pname_marker = cause_pname.find(pname_you);

        if (pname_marker != std::string::npos)
            cause_pname.replace(pname_marker, pname_you.size(), "Sonic Mania");
        v["cause"] = cause_pname;
    }
    Json::StreamWriterBuilder builder;
    b.data                        = Json::writeString(builder, v);
    b.games                       = nullptr;
    b.slots                       = nullptr;
    std::vector<std::string> tags = { std::string("DeathLink") };
    b.tags                        = &tags;
    AP_SendBounce(b);
    //AP_DeathLinkSend(str_reason);
    

}

void ManiaAP_resetDeathLink() {

    sendDeath = 0; }

int ManiaAP_CheckAllMedals(int level) {

    if (level == 1) {
        for (int i = 201; i < 233; i++) {
            if (checkedLocations[i] == 0) {
                return 0;
            }
        }
        return 1;
    }
    else if (level == 2) {
        for (int i = 232; i < 264; i++) {
            if (checkedLocations[i] == 0) {
                return 0;
            }
        }
        return 1;
    }
    return 0;
}



