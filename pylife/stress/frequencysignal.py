import numpy as np
import pandas as pd
from scipy import optimize as op


class psdSignal:
    '''Handles different routines for self signals
    
    Remark: We are using the pandas data frame schema. The index contains the
    discrete frequency step. Every single column one self. 
    
    Some functions of these class: 

    * psd_optimizer
    * ....   
    '''
    def __init__(self,df):
        
        self.df = df
        
    def rms_psd(psd):
        return ((psd.diff()+psd).dropna()).multiply(np.diff(psd.index.values),axis = 0).sum()**0.5
    
    def _intMinlog(Hi,psdin,fsel,factor_rms_nods):
        Ysel =  np.interp(fsel,psdin.index.values,psdin.values.flatten())# an den h-Stuetzstellen
        rms_in = psdSignal.rms_psd(psdin)
        rms_smooth = psdSignal.rms_psd(pd.DataFrame(data = 10**np.interp(psdin.index.values, fsel,np.log10(Hi)),
                                                    index = psdin.index.values))
        eps1 = (rms_in-rms_smooth)**2/rms_in**2
        eps2 =  np.dot(np.log10(Ysel)-np.log10(Hi),np.log10(Ysel)-np.log10(Hi))/np.dot(np.log10(Ysel),np.log10(Ysel))
        return factor_rms_nods*eps1+(1-factor_rms_nods)*eps2
    
    
    def psd_smoother(self,fsel,factor_rms_nodes = 0.5):
        ''' Smooth your PSD using nodes and a penalty factor weighting the errors
        for the RMS and for the node PSD values
        
        Parameters:
        ----------
        
        self: DataFrame
            unsmoothed PSD        
        fsel: list or np.array
           nodes
        factor_rms_nodes: float (0 <= factor_rms_nods <= 1)
            penalty error weighting the errors:
                
            * 0: only error of node PSD values is considered
            * 1: only error of the RMS is considered
            
        Returns:
        --------
        DataFrame        
        '''
    	# InputVariablen
    	# 
        f  = np.logspace(np.log10(self.index.values.min()),np.log10(
                              self.index.values.max()),100)
        # fsel = np.log10(np.unique(np.append(min(f),fsel)))#,max(f)]))
        fsel = np.unique(fsel)
        opt_df = pd.DataFrame()
        for colact in self.columns:
            df_in = pd.DataFrame(data = np.interp(f,self.index.values,self[colact]),
                                 index = f)
            Hi0 = 10**(np.interp(fsel,f,np.log10(df_in.values.flatten())))
            Hi = op.fmin(psdSignal._intMinlog,Hi0,args=(df_in,fsel,factor_rms_nodes),disp = 0)
            opt_df[colact] = np.interp(f,fsel,Hi)
        
        opt_df.index = f            
        return opt_df
    
    