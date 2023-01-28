/* Efficient Projection with Non-negative & Equality Contraint.c
 * Author: Nan LI
 *
 *   min 0.5*|a-a0|^2 + 0.5*|q-q0|^2  st a>=0   ssq>=0   1'a=1'q
 *
 * Input:  a0, q0
 * Output:  a, q
 */
#include <math.h>
#include <string.h>
#include <stdio.h>
#include <malloc.h>

void epne(double* a0, double* q0, double* a, double *q, int m, int n)
{
    int nga=0, nla=0, nea=0, ngq=0, nlq=0, neq=0, nua=m, nuq=n, i, j, k=0, l=0;
    double *vga=(double*)malloc(sizeof(double)*m);
    double *vla=(double*)malloc(sizeof(double)*m);
    double *vgq=(double*)malloc(sizeof(double)*n);
    double *vlq=(double*)malloc(sizeof(double)*n);
    double *vua=a0, *vuq=q0;
    double sa=0.0, sq=0.0, sq0=0.0, rho, val, dsa, dsq, df;

    for(i=0;i<n;i++){// compute the sum of q0
        q0[i]=-q0[i];    sq0+=q0[i];
    }
    while(nua+nuq>0){
        if (nua>0) rho=vua[0]; else rho=vuq[0];    //select the threshold
        dsa=0.0; dsq=0.0;
        nga=0; nla=0; nea=0;
        ngq=0; nlq=0; neq=0;
        for(i=0;i<nua;i++){   // split the vector a
            val=vua[i];
            if (val>rho)        {vga[nga]=val; nga++; dsa+=val;}
            else if (val<rho)   {vla[nla]=val; nla++; }
            else                {dsa+=val; nea++;}
        }
        for(i=0;i<nuq;i++){   // split the vector q
            val=vuq[i];
            if (val>rho)        {vgq[ngq]=val; ngq++; dsq+=val;}
            else if (val<rho)   {vlq[nlq]=val; nlq++; }
        }
        df = sa+dsa+(sq0-sq-dsq)-(k+nga+nea)*rho-(n-l-ngq)*rho;
        if (df<0){
            vua=vla;  nua=nla;  sa+=dsa; k+=(nga+nea);
            vuq=vlq;  nuq=nlq;  sq+=dsq; l+=ngq;
        }else{
            vua=vga;  nua=nga;
            vuq=vgq;  nuq=ngq;
        }
    }
    rho = (sa+sq0-sq)/(k+n-l);
    for(i=0;i<m;i++) {
        val=a0[i]-rho;
        if (val>0) a[i]=val; else a[i]=0.0;
    }
    for(i=0;i<n;i++) {
        q0[i]=-q0[i];
        val=q0[i]+rho;
        if (val>0) q[i]=val; else q[i]=0.0;
    }
    free(vga);free(vla);free(vgq);free(vlq);
}