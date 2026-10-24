
#ifdef __cplusplus
extern "C" {
#endif

void ManiaAP_Init(const char *server, const char *game, const char *slot, const char *password) ;

void ManiaAP_TestSendItem(int) ;

int ManiaAP_hasItem(int) ;

int ManiaAP_checkedLocation(int);

int ManiaAP_Goal(int) ;

int ManiaAP_spheresLevelDone(int);

int ManiaAP_collectRingQueue(void);

void ManiaAP_sendRings(int);

int ManiaAP_checkDeath(void);

void ManiaAP_sendDeath(char *);

void ManiaAP_resetDeathLink(void);

int ManiaAP_CheckAllMedals(int);

#ifdef __cplusplus
}
#endif