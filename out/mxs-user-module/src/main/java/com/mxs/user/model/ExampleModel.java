package com.mxs.user.model;

import javax.persistence.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Set;

@Entity(name = "example")
public class ExampleModel {

    private String codigo;
    private String descricao;
    private int status;
    private LocalDateTime dataCriacao;
    private LocalDateTime dataModificacao;
    private BigDecimal numeroGrande;
    private List<String> listaCompra;
    private Set<BigDecimal> listaVenda;

    public ExampleModel() {}

    public ExampleModel(String codigo, String descricao, int status, LocalDateTime dataCriacao, LocalDateTime dataModificacao, BigDecimal numeroGrande, List<String> listaCompra, Set<BigDecimal> listaVenda) {
        this.codigo = codigo;
        this.descricao = descricao;
        this.status = status;
        this.dataCriacao = dataCriacao;
        this.dataModificacao = dataModificacao;
        this.numeroGrande = numeroGrande;
        this.listaCompra = listaCompra;
        this.listaVenda = listaVenda;
    }

    public String getCodigo() {
	    return codigo;
	}

    public void setCodigo(String codigo) {
	    this.codigo = codigo;
	}

    public String getDescricao() {
	    return descricao;
	}

    public void setDescricao(String descricao) {
	    this.descricao = descricao;
	}

    public int getStatus() {
	    return status;
	}

    public void setStatus(int status) {
	    this.status = status;
	}

    public LocalDateTime getDataCriacao() {
	    return dataCriacao;
	}

    public void setDataCriacao(LocalDateTime dataCriacao) {
	    this.dataCriacao = dataCriacao;
	}

    public LocalDateTime getDataModificacao() {
	    return dataModificacao;
	}

    public void setDataModificacao(LocalDateTime dataModificacao) {
	    this.dataModificacao = dataModificacao;
	}

    public BigDecimal getNumeroGrande() {
	    return numeroGrande;
	}

    public void setNumeroGrande(BigDecimal numeroGrande) {
	    this.numeroGrande = numeroGrande;
	}

    public List<String> getListaCompra() {
	    return listaCompra;
	}

    public void setListaCompra(List<String> listaCompra) {
	    this.listaCompra = listaCompra;
	}

    public Set<BigDecimal> getListaVenda() {
	    return listaVenda;
	}

    public void setListaVenda(Set<BigDecimal> listaVenda) {
	    this.listaVenda = listaVenda;
	}
}
