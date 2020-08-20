// <editor-fold defaultstate="collapsed" desc="EtherCAT Main Initialization Data">

/* SPI or SQI PLIB Interface Initialization for ethercat LAN driver */
const DRV_LAN9253_UTIL_SPI_PLIB_INTERFACE drvLAN9253SpiPlibAPI = {

	/* SPI PLIB WriteRead function */
	.spiWriteRead = (DRV_LAN9253_SPI_PLIB_WRITE_READ)${.vars["${DRV_LAN9253_PLIB?lower_case}"].SPI_PLIB_API_PREFIX}_WriteRead,

	/* SPI PLIB Write function */
	.spiWrite = (DRV_LAN9253_SPI_PLIB_WRITE)${.vars["${DRV_LAN9253_PLIB?lower_case}"].SPI_PLIB_API_PREFIX}_Write,

	/* SPI PLIB Read function */
	.spiRead = (DRV_LAN9253_SPI_PLIB_READ)${.vars["${DRV_LAN9253_PLIB?lower_case}"].SPI_PLIB_API_PREFIX}_Read,

	/* SPI PLIB Transfer Status function */
	.spiIsBusy = (DRV_LAN9253_SPI_PLIB_IS_BUSY)${.vars["${DRV_LAN9253_PLIB?lower_case}"].SPI_PLIB_API_PREFIX}_IsBusy,

	/* SPI PLIB Callback Register */
	.spiCallbackRegister = (DRV_LAN9253_SPI_PLIB_CALLBACK_REGISTER)${.vars["${DRV_LAN9253_PLIB?lower_case}"].SPI_PLIB_API_PREFIX}_CallbackRegister,
};

const DRV_LAN9253_UTIL_TMR_PLIB_INTERFACE drvLAN9253TimerPlibAPI = {

	.timerCallbackSet = (DRV_LAN9253_TMR_PLIB_CALLBACK_REGISTER)${.vars["${DRV_LAN9253_TIMER_PLIB?lower_case}"].CALLBACK_API_NAME},
	
	.timerStart = (DRV_LAN9253_TMR_PLIB_START)${.vars["${DRV_LAN9253_TIMER_PLIB?lower_case}"].TIMER_START_API_NAME},
	
	.timerStop = (DRV_LAN9253_TMR_PLIB_STOP)${.vars["${DRV_LAN9253_TIMER_PLIB?lower_case}"].TIMER_STOP_API_NAME},
};

/* LAN9253 Driver Initialization Data */
const DRV_LAN9253_UTIL_INIT drvLAN9253InitData = {

	/* SPI PLIB API  interface*/
	.spiPlib = &drvLAN9253SpiPlibAPI,
	
	/* Timer PLIB API Interface */
	.timerPlib = &drvLAN9253TimerPlibAPI,

};

// </editor-fold>