// ---------------------------------------------------------------------
// RSDK Project: Sonic Mania
// Object Description: LevelSelect Object
// Object Author: Christian Whitehead/Simon Thomley/Hunter Bridges
// Decompiled by: Rubberduckycooly & RMGRich
// ---------------------------------------------------------------------

#include "Game.h"
#include "ManiaAP.h"

ObjectLevelSelect *LevelSelect;

void LevelSelect_Update(void)
{
    RSDK_THIS(LevelSelect);

#if MANIA_USE_PLUS
    EntityUIText *text = self->pinballLabel;
    if (text)
        text->visible = API.CheckDLC(DLC_PLUS);
#endif

    StateMachine_Run(self->state);

    ScreenInfo->position.x = 0x100 - ScreenInfo->center.x;
    //check for new items
    for (int16 i = 0; i < 50; i++) {
        globals->unlockedItems[i] = ManiaAP_hasItem(i);
    }
    globals->unlockedItems[99] = ManiaAP_hasItem(99);//chaos emeralds

    

}

void LevelSelect_LateUpdate(void) {}

void LevelSelect_StaticUpdate(void)
{
    if (--LevelSelect->bgAniDuration <= 0) {
        ++LevelSelect->bgAniFrame;

        LevelSelect->bgAniFrame &= 3;
        LevelSelect->bgAniDuration = LevelSelect->bgAniDurationTable[LevelSelect->bgAniFrame];

        TileLayer *background = RSDK.GetTileLayer(0);
        background->scrollPos = (background->scrollPos + 0x1000000) & 0x7FF0000;
    }
}

void LevelSelect_Draw(void)
{
    RSDK_THIS(LevelSelect);





    StateMachine_Run(self->stateDraw);


    
}

void LevelSelect_Create(void *data)
{
    RSDK_THIS(LevelSelect);

    if (!SceneInfo->inEditor) {
        self->active    = ACTIVE_ALWAYS;
        self->visible   = true;
        self->drawGroup = 12;
        self->state     = LevelSelect_State_Init;
        self->stateDraw = LevelSelect_Draw_Fade;
        self->timer     = 640;
    }

    String tag;
    INIT_STRING(tag);
    RSDK.InitString(&tag, "X", 0x1);
    int i = 0;
    for (int16 i = 0; i < 50; i++) {
        globals->unlockedItems[i] = ManiaAP_hasItem(i);
    }
    foreach_all(UIText, label)
    {
        if (label->align == UITEXT_ALIGN_RIGHT) {
            
    // self->stageIDLabels[i]->text.chars[0] = '1';
    //  self->stageIDLabels[i]->text = tag;
            if (globals->unlockedItems[i + 6] == 0 && i<20) {
                RSDK.SetString(&label->text, "X");
            }
            else if (globals->unlockedItems[25]==0 && i == 20) {
                RSDK.SetString(&label->text, "X");
            }
            else if (globals->unlockedItems[i+5] == 0 && i<25 && i>20) {
                RSDK.SetString(&label->text, "X");
            }
            else if (globals->unlockedItems[99] < 7 && i == 25) {
                RSDK.SetString(&label->text, "X");
            }

        //LogHelpers_Print("i: %d", i);
        //LogHelpers_Print("data0: %d", label->data0);
        //LogHelpers_Print("data1: %d", label->data1);
        //LogHelpers_Print("data2: %d", label->data2);
    // RSDK.DrawText(&label->animator, &drawPos, &tag, 0, &tag.length, ALIGN_CENTER, 0, NULL, NULL, false);
    //RSDK.AppendString(&label->text, &tag);

    //
        i++;
        }
    }


}

void LevelSelect_StageLoad(void)
{
    LevelSelect->sfxFail = RSDK.GetSfx("Stage/Fail.wav");
#if MANIA_USE_PLUS
    LevelSelect->sfxRing     = RSDK.GetSfx("Global/Ring.wav");
    LevelSelect->sfxEmerald  = RSDK.GetSfx("Special/Emerald.wav");
    LevelSelect->sfxContinue = RSDK.GetSfx("Special/Continue.wav");
    LevelSelect->sfxMedalGot = RSDK.GetSfx("Special/MedalCaught.wav");
#endif

    RSDK.ResetEntitySlot(0, LevelSelect->classID, NULL);

    UIPicture->aniFrames = RSDK.LoadSpriteAnimation("LSelect/Icons.bin", SCOPE_STAGE);
    UIText->aniFrames    = RSDK.LoadSpriteAnimation("LSelect/Text.bin", SCOPE_STAGE);

    LevelSelect->startMusicID = 0;
    LevelSelect->soundTestMax = 0;
    foreach_all(Music, music)
    {
        if (!LevelSelect->startMusicID) {
            LevelSelect->startMusicID = RSDK.GetEntitySlot(music);
        }
        ++LevelSelect->soundTestMax;
    }
    ++LevelSelect->startMusicID;
    --LevelSelect->soundTestMax;

    globals->medalMods |= MEDAL_DEBUGMODE;
#if MANIA_USE_PLUS
    LevelSelect->cheatCodePtrs[0] = LevelSelect->cheat_RickyMode;
    LevelSelect->cheatCodePtrs[1] = LevelSelect->cheat_AllEmeralds;
    LevelSelect->cheatCodePtrs[2] = LevelSelect->cheat_MaxContinues;
    LevelSelect->cheatCodePtrs[3] = LevelSelect->cheat_SwapGameMode;
    LevelSelect->cheatCodePtrs[4] = LevelSelect->cheat_UnlockAllMedals;
    LevelSelect->cheatCodePtrs[5] = LevelSelect->cheat_SuperDash;
    LevelSelect->cheatCodePtrs[6] = LevelSelect->cheat_MaxControl;
    LevelSelect->cheatCodePtrs[7] = LevelSelect->cheat_ToggleSuperMusic;

    LevelSelect->checkCheatActivated[0] = LevelSelect_Cheat_RickyMode;
    LevelSelect->checkCheatActivated[1] = LevelSelect_Cheat_AllEmeralds;
    LevelSelect->checkCheatActivated[2] = LevelSelect_Cheat_MaxContinues;
    LevelSelect->checkCheatActivated[3] = LevelSelect_Cheat_SwapGameMode;
    LevelSelect->checkCheatActivated[4] = LevelSelect_Cheat_UnlockAllMedals;
    LevelSelect->checkCheatActivated[5] = LevelSelect_Cheat_SuperDash;
    LevelSelect->checkCheatActivated[6] = LevelSelect_Cheat_MaxControl;
    LevelSelect->checkCheatActivated[7] = LevelSelect_Cheat_ToggleSuperMusic;

    LevelSelect->cheatCodePos[0] = 0;
    LevelSelect->cheatCodePos[1] = 0;
    LevelSelect->cheatCodePos[2] = 0;
    LevelSelect->cheatCodePos[3] = 0;
    LevelSelect->cheatCodePos[4] = 0;
    LevelSelect->cheatCodePos[5] = 0;
    LevelSelect->cheatCodePos[6] = 0;
    LevelSelect->cheatCodePos[7] = 0;
#endif
}

#if MANIA_USE_PLUS
void LevelSelect_Cheat_AllEmeralds(void)
{
    Music_FadeOut(0.125);
    RSDK.PlaySfx(LevelSelect->sfxEmerald, false, 255);

    for (int32 e = 0; e < 7; ++e) SaveGame_SetEmerald(e);
}

void LevelSelect_Cheat_ToggleSuperMusic(void)
{
    RSDK.PlaySfx(LevelSelect->sfxRing, false, 255);
    globals->superMusicEnabled ^= 1;
}

void LevelSelect_Cheat_MaxContinues(void)
{
    RSDK.PlaySfx(LevelSelect->sfxContinue, false, 255);
    SaveGame_GetSaveRAM()->continues = 14;
}

void LevelSelect_Cheat_MaxControl(void)
{
    RSDK.PlaySfx(LevelSelect->sfxRing, false, 255);
    globals->medalMods &= ~MEDAL_NODROPDASH;
    globals->medalMods |= MEDAL_INSTASHIELD;
    globals->medalMods |= MEDAL_PEELOUT;
}

void LevelSelect_Cheat_RickyMode(void)
{
    RSDK.PlaySfx(LevelSelect->sfxRing, false, 255);
    globals->secrets ^= SECRET_RICKYMODE;
}

void LevelSelect_Cheat_SuperDash(void)
{
    RSDK.PlaySfx(LevelSelect->sfxRing, false, 255);
    globals->secrets ^= SECRET_SUPERDASH;
}

void LevelSelect_Cheat_SwapGameMode(void)
{
    if (API.CheckDLC(DLC_PLUS)) {
        RSDK.PlaySfx(LevelSelect->sfxRing, false, 255);
        if (globals->gameMode == MODE_ENCORE) {
            globals->gameMode = MODE_MANIA;
        }
        else {
            globals->gameMode = MODE_ENCORE;
            if (globals->medalMods & MEDAL_ANDKNUCKLES) 
                globals->medalMods &= ~MEDAL_ANDKNUCKLES;
        }
    }
}

void LevelSelect_Cheat_UnlockAllMedals(void)
{
    if (globals->superSecret && (globals->secrets & SECRET_RICKYMODE)) {
        RSDK.PlaySfx(LevelSelect->sfxMedalGot, false, 255);
        GameProgress_UnlockAll();
        GameProgress_LockAllSpecialClear();
    }
    else {
        RSDK.PlaySfx(LevelSelect->sfxRing, false, 255);
    }
}
#endif

void LevelSelect_Draw_Fade(void)
{
    RSDK_THIS(LevelSelect);
    RSDK.FillScreen(0x000000, self->timer, self->timer - 128, self->timer - 256);
}

void LevelSelect_State_Init(void)
{
    RSDK_THIS(LevelSelect);

    int32 labelPos[32];
    int32 lastY = 0;

        // X out acts that havent been obtained
    //  draw X's near act icons for locked levels




    //foreach_all(UIText, label)
    //{

                //self->stageIDLabels[i]->text.chars[0] = '1';
                // self->stageIDLabels[i]->text = tag;
                // RSDK.SetString(&self->stageIDLabels[i]->text, "X");

                //RSDK.DrawText(&label->animator, &drawPos, &tag, 0, &tag.length, ALIGN_CENTER, 0, NULL, NULL, false);
                //RSDK.AppendString(&label->text, &tag);

    //
    //}

    foreach_all(UIText, labelPosPtrL)
    {
        if (labelPosPtrL->position.x < 0x1000000 && labelPosPtrL->position.y > lastY) {
            lastY                        = labelPosPtrL->position.y;
            labelPos[self->labelCount++] = labelPosPtrL->position.y;
        }
    }

    foreach_all(UIText, labelL)
    {
        if (labelL->position.x < 0x1000000) {
            for (int32 i = 0; i < self->labelCount; ++i) {
                if (labelL->position.y == labelPos[i]) {
                    switch (labelL->align) {
                        case UITEXT_ALIGN_LEFT: self->zoneNameLabels[i] = labelL; break;

                        default:
                        case UITEXT_ALIGN_CENTER: break;

                        case UITEXT_ALIGN_RIGHT: self->stageIDLabels[i] = labelL; break;
                    }
                }
            }
        }
    }

    if (self->labelCount > 0)
        memset(labelPos, 0, sizeof(int32) * self->labelCount);

    lastY = 0;

    foreach_all(UIText, labelPosPtrR)
    {
        if (labelPosPtrR->position.x > 0x1000000 && labelPosPtrR->position.y > lastY) {
            lastY                        = labelPosPtrR->position.y;
            labelPos[self->labelCount++] = labelPosPtrR->position.y;
        }
    }

    foreach_all(UIText, labelR)
    {
        if (labelR->position.x > 0x1000000 && self->labelCount > 0) {
            for (int32 i = 0; i < self->labelCount; ++i) {
                if (labelR->position.y == labelPos[i]) {
                    switch (labelR->align) {
                        case UITEXT_ALIGN_LEFT: self->zoneNameLabels[i] = labelR; break;

                        default:
                        case UITEXT_ALIGN_CENTER: break;

                        case UITEXT_ALIGN_RIGHT: self->stageIDLabels[i] = labelR;
#if MANIA_USE_PLUS
                            if (!labelR->data0 && labelR->data1 == 15)
                                self->pinballLabel = labelR;
#endif
                            break;
                    }
                }
            }
        }
    }

    for (int32 i = 0; i < self->labelCount; ++i) {
        if (!self->zoneNameLabels[i]) {
            for (int32 v = i; v >= 0; --v) {
                if (self->zoneNameLabels[v]) {
                    self->zoneNameLabels[i] = self->zoneNameLabels[v];
                    break;
                }
            }
        }
    }

    LevelSelect_SetLabelHighlighted(true);

    foreach_all(UIText, soundTestLabel)
    {
        if (soundTestLabel->align == UITEXT_ALIGN_CENTER) {
            self->soundTestLabel  = soundTestLabel;
            soundTestLabel->align = UITEXT_ALIGN_LEFT;
        }
    }

    self->leaderCharacterID   = HUD_CharacterIndexFromID(GET_CHARACTER_ID(1)) + 1;
    self->sidekickCharacterID = HUD_CharacterIndexFromID(GET_CHARACTER_ID(2)) + 1;

    foreach_all(UIPicture, picture)
    {
        if (picture->listID == 1) {
            self->zoneIcon = picture;

            // Bug Details(?):
            // frameID is equal to... playerID...?
            // this feels like a slight oversight, though idk what it is meant to be
            picture->animator.frameID = self->leaderCharacterID;
        }
        else if (picture->listID == 3) {
            if (picture->frameID)
                self->player2Icon = picture;
            else
                self->player1Icon = picture;
        }
    }

    self->stageIDLabels[self->labelCount - 1] = self->soundTestLabel;

    LevelSelect_ManagePlayerIcon();


    String tag;
    INIT_STRING(tag);
    RSDK.InitString(&tag, "X", 0x1);

    for (int i = 0; i < 32; i++) {

        //if (self->stageIDLabels[i]->data0 != 0) {
        //    self->stageIDLabels[i]->text.chars[0] = 'a';
        //}
            

            //RSDK.SetString(&self->stageIDLabels[i]->text, "X");

            //RSDK.AppendString(&self->stageIDLabels[i]->text, &tag);
            
    }





    self->state = LevelSelect_State_FadeIn;
}

void LevelSelect_State_FadeIn(void)
{
    RSDK_THIS(LevelSelect);

    if (self->timer <= 0) {
        self->timer     = 0;
        self->state     = LevelSelect_State_Navigate;
        self->stateDraw = StateMachine_None;
    }
    else {
        self->timer -= 16;
    }

    LevelSelect_ManagePlayerIcon();




}

void LevelSelect_State_Navigate(void)
{
    RSDK_THIS(LevelSelect);

    bool32 confirmPress = API_GetConfirmButtonFlip() ? ControllerInfo->keyB.press : ControllerInfo->keyA.press;

    if (ControllerInfo->keyUp.down || AnalogStickInfoL->keyUp.down) {
        self->timer = (self->timer + 1) & 0xF;

        if (self->timer == 1) {
            LevelSelect_SetLabelHighlighted(false);
#if MANIA_USE_PLUS
            if (--self->labelID == 28 && !API.CheckDLC(DLC_PLUS))
#endif
                --self->labelID;

            if (self->labelID < 0)
                self->labelID = self->labelCount - 1;

            LevelSelect_SetLabelHighlighted(true);
        }
    }
    else if (ControllerInfo->keyDown.down || AnalogStickInfoL->keyDown.down) {
        self->timer = (self->timer + 1) & 0xF;
        if (self->timer == 1) {
            LevelSelect_SetLabelHighlighted(false);

#if MANIA_USE_PLUS
            if (++self->labelID == 28 && !API.CheckDLC(DLC_PLUS))
#endif
                ++self->labelID;

            if (self->labelID == self->labelCount)
                self->labelID = 0;

            LevelSelect_SetLabelHighlighted(true);
        }
    }
    else if (AnalogStickInfoL->keyLeft.press || ControllerInfo->keyLeft.press || ControllerInfo->keyRight.press || AnalogStickInfoL->keyRight.press) {
        self->timer = 0;

        if (self->labelID >= self->labelCount - 1) {
            if (AnalogStickInfoL->keyLeft.press || ControllerInfo->keyLeft.press) {
                if (--self->soundTestID < 0)
                    self->soundTestID = LevelSelect->soundTestMax - 1;
            }
            else if (++self->soundTestID >= LevelSelect->soundTestMax) {
                self->soundTestID = 0;
            }

            EntityUIText *soundTest  = self->soundTestLabel;
            soundTest->text.chars[0] = self->soundTestID >> 4;
            soundTest->text.chars[1] = self->soundTestID & 0xF;
        }
        else {
            LevelSelect_HandleColumnChange();
        }
    }
    else if (confirmPress || ControllerInfo->keyStart.press) {
        if (self->labelID < self->labelCount - 1 || ControllerInfo->keyStart.press) {
#if MANIA_USE_PLUS
            if (self->labelID != 28 || API.CheckDLC(DLC_PLUS))
                LevelSelect_HandleNewStagePos();
            else
                RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
#else
            LevelSelect_HandleNewStagePos();
#endif
        }
        else {
            EntityMusic *track = RSDK_GET_ENTITY(self->soundTestID + LevelSelect->startMusicID, Music);
            Music_PlayTrackPtr(track);

#if MANIA_USE_PLUS
            self->offsetUFO = self->soundTestID % 14;
            self->offsetBSS = self->soundTestID & 0x1F;
            for (int32 i = 0; i < 8; ++i) {
                if (self->soundTestID != LevelSelect->cheatCodePtrs[i][LevelSelect->cheatCodePos[i]]) {
                    LevelSelect->cheatCodePos[i] = 0;
                }
                else {
                    LevelSelect->cheatCodePos[i]++;
                    if (LevelSelect->cheatCodePtrs[i][LevelSelect->cheatCodePos[i]] == 255) {
                        LevelSelect->checkCheatActivated[i]();
                        LevelSelect->cheatCodePos[i] = 0;
                    }
                }
            }
#endif
        }
    }
#if GAME_VERSION == VER_100
    else if (TouchInfo->count) {

        self->timer = (self->timer + 1) & 0xF;
        if (self->timer == 1) {
            int32 selectedLabel = -1;

            int32 labelID = self->labelCount - 1;
            for (int32 l = 0; l < self->labelCount; ++l, labelID--) {
                EntityUIText *label = self->zoneNameLabels[labelID];

                if (label && labelID != self->labelID) {
                    int32 xOff = 5 * (label->text.length * 0.5);

                    for (int32 f = 0; f < TouchInfo->count; ++f) {
                        float tx = TouchInfo->x[f] * ScreenInfo->size.x;
                        float ty = TouchInfo->y[f] * ScreenInfo->size.y;

                        if (tx > ((label->position.x >> 16) - xOff) && tx < (xOff + (label->position.x >> 16))) {
                            if (ty < ((label->position.y >> 16) + 10) && ty > ((label->position.y >> 16) - 10))
                                selectedLabel = labelID;
                        }
                    }
                }
            }

            if (selectedLabel == -1) {
                labelID = self->labelCount - 1;
                for (int32 l = 0; l < self->labelCount; ++l) {
                    EntityUIText *label = self->stageIDLabels[labelID];

                    if (label && labelID != self->labelID) {
                        int32 xOff = 5 * (label->text.length * 0.5);

                        for (int32 f = 0; f < TouchInfo->count; ++f) {
                            float tx = TouchInfo->x[f] * ScreenInfo->size.x;
                            float ty = TouchInfo->y[f] * ScreenInfo->size.y;

                            if (tx > ((label->position.x >> 16) - xOff) && tx < (xOff + (label->position.x >> 16))) {
                                if (ty < ((label->position.y >> 16) + 10) && ty > ((label->position.y >> 16) - 10))
                                    selectedLabel = labelID;
                            }
                        }
                    }
                    labelID--;
                }
            }

            for (int32 f = 0; f < TouchInfo->count; ++f) {
                float tx = TouchInfo->x[f] * ScreenInfo->size.x;
                float ty = TouchInfo->y[f] * ScreenInfo->size.y;

                if (tx > 250.0 && ty > 170.0 && tx < 310.0 && ty < 230.0)
                    LevelSelect_HandleNewStagePos();
            }

            if (selectedLabel != -1) {
                LevelSelect_SetLabelHighlighted(false);
                self->labelID = selectedLabel;
                LevelSelect_SetLabelHighlighted(true);
            }
        }
    }
#endif
    else {
        self->timer = 0;
    }

    if (ControllerInfo->keyX.press) {
        ++self->leaderCharacterID;
        LevelSelect_ManagePlayerIcon();
    }

    if (ControllerInfo->keyY.press) {
        ++self->sidekickCharacterID;
        LevelSelect_ManagePlayerIcon();
    }

    EntityUIPicture *zoneIcon = self->zoneIcon;
    if (self->labelID >= self->labelCount - 1)
        RSDK.SetSpriteAnimation(UIPicture->aniFrames, 2, &zoneIcon->animator, true, self->leaderCharacterID);
    else
        RSDK.SetSpriteAnimation(UIPicture->aniFrames, 1, &zoneIcon->animator, true, self->stageIDLabels[self->labelID]->data1);
}

void LevelSelect_State_FadeOut(void)
{
    RSDK_THIS(LevelSelect);

    if (self->timer >= 1024)
        RSDK.LoadScene();
    else
        self->timer += 16;
}

void LevelSelect_ManagePlayerIcon(void)
{
    RSDK_THIS(LevelSelect);

    self->leaderCharacterID %= 5;
    if (self->leaderCharacterID == 0) {
        self->leaderCharacterID++;
    }
    //change self->leaderCharacterID based on unlocked characters
    for (int16 i = 1;i<5;i++) {
        if (self->leaderCharacterID == i) {
            if (globals->unlockedItems[i] == 0) {
                self->leaderCharacterID += 1;
            }
        }
    }
    if (self->leaderCharacterID >= LSELECT_PLAYER_RAY) {//loop through again to find a valid char
        if (globals->unlockedItems[5] == 0) {
            self->leaderCharacterID == LSELECT_PLAYER_SONIC;
            for (int16 i = 1; i < 5; i++) {
                if (self->leaderCharacterID == i) {
                    if (globals->unlockedItems[i] == 0) {
                        self->leaderCharacterID += 1;
                        if (self->leaderCharacterID == LSELECT_PLAYER_RAY && globals->unlockedItems[5] == 0) {
                            self->leaderCharacterID = LSELECT_PLAYER_SONIC;// still havent found a valid char, default to sonic
                            break;
                        } 
                    }
                }
            }

        }
    }





    EntityUIPicture *player1 = self->player1Icon;
    EntityUIPicture *player2 = self->player2Icon;

    switch (self->leaderCharacterID) {
        case LSELECT_PLAYER_SONIC:
        case LSELECT_PLAYER_TAILS:
        //    // Bug Details(?):
        //    if (self->sidekickCharacterID == LSELECT_PLAYER_TAILS) // if leader is sonic or tails, and the sidekick is tails... change to knux...?
        //        self->leaderCharacterID = LSELECT_PLAYER_KNUCKLES;
            // playerID 3 may have been meant to be "S&T" before it was rearranged?
            // v4 support this, with the player ids being: Sonic, Tails, Knux, Sonic & Tails

            player1->animator.frameID = self->leaderCharacterID;
            break;

        case LSELECT_PLAYER_KNUCKLES: player1->animator.frameID = self->leaderCharacterID; break;

#if MANIA_USE_PLUS
        case LSELECT_PLAYER_MIGHTY:
        case LSELECT_PLAYER_RAY:
            if (!API.CheckDLC(DLC_PLUS))
                self->leaderCharacterID = LSELECT_PLAYER_SONIC;

            player1->animator.frameID = self->leaderCharacterID;
            break;
#endif

        default:
            self->leaderCharacterID   = LSELECT_PLAYER_SONIC;
            player1->animator.frameID = LSELECT_PLAYER_SONIC;
            break;
    }

    switch (self->sidekickCharacterID) {
        case LSELECT_PLAYER_TAILS:
            player2->animator.frameID = self->sidekickCharacterID;

            // if leader is sonic & sidekick is tails, show ST icon. otherwise remove sidekick
            if (self->leaderCharacterID != LSELECT_PLAYER_SONIC) {
                self->sidekickCharacterID = LSELECT_PLAYER_NONE;
                player2->animator.frameID = LSELECT_PLAYER_NONE;
            }
            break;

        default:
            self->sidekickCharacterID = LSELECT_PLAYER_NONE;
            player2->animator.frameID = LSELECT_PLAYER_NONE;
            break;

        // if P2 is sonic, no he's not thats tails actually
        case LSELECT_PLAYER_SONIC:
            self->sidekickCharacterID = LSELECT_PLAYER_TAILS;
            player2->animator.frameID = LSELECT_PLAYER_TAILS;

            // if leader is sonic & sidekick is tails, show ST icon. otherwise remove sidekick
            if (self->leaderCharacterID != LSELECT_PLAYER_SONIC) {
                self->sidekickCharacterID = LSELECT_PLAYER_NONE;
                player2->animator.frameID = LSELECT_PLAYER_NONE;
            }
            break;
    }
}

void LevelSelect_SetLabelHighlighted(bool32 highlight)
{
    RSDK_THIS(LevelSelect);

    EntityUIText *zoneName = self->zoneNameLabels[self->labelID];
    if (zoneName)
        zoneName->highlighted = highlight;

    EntityUIText *stageID = self->stageIDLabels[self->labelID];
    if (stageID)
        stageID->highlighted = highlight;
}

void LevelSelect_HandleColumnChange(void)
{
    RSDK_THIS(LevelSelect);

    EntityUIText *curLabel = self->stageIDLabels[self->labelID];
    if (!curLabel)
        curLabel = self->zoneNameLabels[self->labelID];

    int32 distance         = 0x1000000;
    EntityUIText *labelPtr = NULL;
    if (curLabel->position.x < 0x1000000) {
        foreach_active(UIText, label)
        {
            if (label->position.x > 0x1000000) {
                int32 pos = abs(label->position.y - curLabel->position.y);
                if (pos < distance) {
                    distance = pos;
                    labelPtr = label;
                }
            }
        }
    }
    else {
        foreach_active(UIText, label)
        {
            if (label->position.x < 0x1000000) {
                int32 dist = abs(label->position.y - curLabel->position.y);
                if (dist < distance) {
                    distance = dist;
                    labelPtr = label;
                }
            }
        }
    }

    int32 labelID = self->labelID;
    for (int32 i = 0; i < self->labelCount; ++i) {
        if (self->stageIDLabels[i] == labelPtr || self->zoneNameLabels[i] == labelPtr) {
            labelID = i;
            break;
        }
    }

    if (self->labelID != labelID) {
        LevelSelect_SetLabelHighlighted(false);

        self->labelID = labelID;
        LevelSelect_SetLabelHighlighted(true);
    }
}

void LevelSelect_HandleNewStagePos(void)
{
    RSDK_THIS(LevelSelect);

    EntityUIText *curLabel = self->stageIDLabels[self->labelID];
    if (!curLabel)
        curLabel = self->zoneNameLabels[self->labelID];
    LogHelpers_Print("data0 %d", curLabel->data0);
    if (self->labelID != self->labelCount - 4) {
    for (int16 i = 0; i < 12; i++) {

        if (curLabel->data0 == i) {
            if (globals->unlockedItems[i + 6] == 0) {
                RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
                return;
            }
        }
    }

    if (curLabel->data0 == 13) {
        if (globals->unlockedItems[18] == 0) {
            RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
            return;
        }
    }
    if (curLabel->data0 == 14) {
        if (globals->unlockedItems[19] == 0) {
            RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
            return;
        }
    }
    if (curLabel->data0 == 15) {
        if (globals->unlockedItems[20] == 0) {
            RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
            return;
        }
    }

    if (curLabel->data0 == 17) {
        if (globals->unlockedItems[21] == 0) {
            RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
            return;
        }
    }
    if (curLabel->data0 == 18) {
        if (globals->unlockedItems[22] == 0) {
            RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
            return;
        }
    }

    if (curLabel->data0 == 19) {
        if (globals->unlockedItems[23] == 0) {
            RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
            return;
        }
    }
    if (curLabel->data0 == 20) {
        if (globals->unlockedItems[24] == 0) {
            RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
            return;
        }
    }
    if (curLabel->data0 == 21 || curLabel->data0 == 22) {
        if (globals->unlockedItems[25] == 0) {
            RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
            return;
        }
    }
    if (curLabel->data0 == 23) {
        if (globals->unlockedItems[26] == 0) {
            RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
            return;
        }
    }
    if (curLabel->data0 == 24) {
        if (globals->unlockedItems[27] == 0) {
            RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
            return;
        }
    }
    if (curLabel->data0 == 25) {
        if (globals->unlockedItems[28] == 0) {
            RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
            return;
        }
    }
    if (curLabel->data0 == 26) {
        if (globals->unlockedItems[29] == 0) {
            RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
            return;
        }
    }
    if (self->labelID == self->labelCount - 5) {
        if (globals->unlockedItems[99] < 7) {
            RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
            return;
        }
    }
    }
    else {
        for (int16 i = 0; i < 8; i++) {

            if (self->offsetUFO == i) {
                if (globals->unlockedItems[i + 30] == 0) {
                    RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
                    return;
                }
            }
        }
    
    }

    globals->enableIntro = false;
    

    if (curLabel->selectable) {
        char buffer[32];
        RSDK.GetCString(buffer, &curLabel->tag);

        RSDK.SetScene(buffer, "");
        SceneInfo->listPos += curLabel->data0;

#if MANIA_USE_PLUS
        if (self->labelID == self->labelCount - 4)
            SceneInfo->listPos += self->offsetUFO;
        else if (self->labelID == self->labelCount - 3)
            SceneInfo->listPos += self->offsetBSS;
        else if (globals->gameMode == MODE_ENCORE)
            SceneInfo->listPos = Zone_GetListPos_EncoreMode();
#endif

        int32 leaderID = 0;
        if (self->leaderCharacterID > 0)
            leaderID = 1 << (self->leaderCharacterID - 1);

        int32 sidekickID = 0;
        if (self->sidekickCharacterID > 0)
            sidekickID = 1 << (self->sidekickCharacterID - 1);

        globals->playerID = leaderID | (sidekickID << 8);

        // MSZ1K check
        if (CHECK_CHARACTER_ID(ID_KNUCKLES, 1) && curLabel->data0 == 15)
            ++SceneInfo->listPos;

        self->timer     = 0;
        self->state     = LevelSelect_State_FadeOut;
        self->stateDraw = LevelSelect_Draw_Fade;
        Music_FadeOut(0.1);
    }
    else {
        RSDK.PlaySfx(LevelSelect->sfxFail, false, 255);
    }
}

#if GAME_INCLUDE_EDITOR
void LevelSelect_EditorDraw(void) {}

void LevelSelect_EditorLoad(void)
{
    if (UIPicture)
        UIPicture->aniFrames = RSDK.LoadSpriteAnimation("LSelect/Icons.bin", SCOPE_STAGE);

    if (UIText)
        UIText->aniFrames = RSDK.LoadSpriteAnimation("LSelect/Text.bin", SCOPE_STAGE);
}
#endif

void LevelSelect_Serialize(void) {}
