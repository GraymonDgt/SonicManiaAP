
#ifdef __cplusplus
extern "C" {
#endif

void ManiaAP_Init(const char *server, const char *game, const char *slot, const char *password) ;

void ManiaAP_SendItem(int item) ;

int ManiaAP_hasItem(int id) ;

void ManiaAP_Goal(void) ;

#ifdef __cplusplus
}
#endif