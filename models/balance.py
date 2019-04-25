class balance():
    """
    Class Balance.
    """

    def __init__(self, ativo_total: float, ativo_circulante: float, ac_caixa_e_equivalentes_de_caixa: float,
                 ac_aplicaçoes_financeiras: float,
                 ac_contas_a_receber: float, ac_estoques: float, ac_ativos_biologicos: float,
                 ac_tributos_a_recuperar: float, ac_despesas_antecipadas: float,
                 ac_outros_ativos: float, ativo_nao_circulante: float,
                 anc_aplicacoes_financeiras_avaliadas_a_valor_justo: float,
                 anc_aplicaçoes_financeiras_avaliadas_ao_custo_amortizado: float, anc_contas_a_receber: float,
                 anc_estoques: float, anc_ativos_biologicos: float,
                 anc_tributos_diferidos: float, anc_despesas_antecipadas: float,
                 anc_creditos_com_partes_relacionadas: float,
                 anc_outros_ativos: float, anc_investimentos: float, anc_imobilizado: float, anc_intangivel: float,
                 anc_diferido: float,
                 passivo_total: float, passivo_circulante: float, pc_obrigacoes_sociais_e_trabalhistas: float,
                 pc_fornecedores: float, pc_obrigacoes_fiscais: float, pc_emprestimos_e_financiamentos: float,
                 pc_passivos_com_partes_relacionadas: float, pc_dividendos_e_jcp_a_pagar: float, pc_outros: float,
                 pc_provisoes: float,
                 pc_passivos_sobre_ativos_nao_correntes_a_venda_e_descontinuados: float,
                 passivo_nao_circulante_: float, pnc_emprestimos_e_financiamentos: float,
                 pnc_passivos_com_partes_relacionadas: float, pnc_outros: float, pnc_tributos_diferidos: float,
                 pnc_adiantamento_para_futuro_aumento_capital: float, pnc_provisoes: float,
                 pnc_passivos_sobre_ativos_nao_correntes_a_venda_e_descontinuados: float,
                 pnc_lucros_e_receitas_a_apropriar: float,
                 pnc_participacao_dos_acionistas_nao_controladores: float, patrimonio_liquido: float,
                 pl_capital_social_realizado: float,
                 reservas_de_capital: float, pl_reservas_de_reavaliacao: float, pl_reservas_de_lucros: float,
                 pl_lucros_prejuizos_acumulados: float,
                 pl_ajustes_de_avaliacao_patrimonial: float, pl_ajustes_acumulados_de_conversao: float,
                 pl_outros_resultados_abrangentes: float,
                 pl_adiantamento_para_futuro_aumento_capital: float):
        """

        """
        self.ativo_total = float(ativo_total)
        self.ativo_circulante = float(ativo_circulante)
        self.ativo_total = float(ativo_total)
        self.ac_caixa_e_equivalentes_de_caixa = float(ac_caixa_e_equivalentes_de_caixa)
        self.ac_aplicaçoes_financeiras = float(ac_aplicaçoes_financeiras)
        self.ac_contas_a_receber = float(ac_contas_a_receber)
        self.ac_estoques = float(ac_estoques)
        self.ac_ativos_biologicos = float(ac_ativos_biologicos)
        self.ac_tributos_a_recuperar = float(ac_tributos_a_recuperar)
        self.ac_despesas_antecipadas = float(ac_despesas_antecipadas)
        self.ac_outros_ativos = float(ac_outros_ativos)
        self.ativo_nao_circulante = float(ativo_nao_circulante)
        self.anc_aplicacoes_financeiras_avaliadas_a_valor_justo = float(anc_aplicacoes_financeiras_avaliadas_a_valor_justo)
        self.anc_aplicaçoes_financeiras_avaliadas_ao_custo_amortizado = float(anc_aplicaçoes_financeiras_avaliadas_ao_custo_amortizado)
        self.anc_contas_a_receber = float(anc_contas_a_receber)
        self.anc_estoques = float(anc_estoques)
        self.anc_ativos_biologicos = float(anc_ativos_biologicos)
        self.anc_tributos_diferidos = float(anc_tributos_diferidos)
        self.anc_despesas_antecipadas = float(anc_despesas_antecipadas)
        self.anc_creditos_com_partes_relacionadas = float(anc_creditos_com_partes_relacionadas)
        self.anc_outros_ativos = float(anc_outros_ativos)
        self.anc_investimentos = float(anc_investimentos)
        self.anc_imobilizado = float(anc_imobilizado)
        self.anc_intangivel = float(anc_intangivel)
        self.anc_diferido = float(anc_diferido)
        self.passivo_total = float(passivo_total)
        self.passivo_circulante = float(passivo_circulante)
        self.pc_obrigacoes_sociais_e_trabalhistas = float(pc_obrigacoes_sociais_e_trabalhistas)
        self.pc_fornecedores = float(pc_fornecedores)
        self.pc_obrigacoes_fiscais = float(pc_obrigacoes_fiscais)
        self.pc_emprestimos_e_financiamentos = float(pc_emprestimos_e_financiamentos)
        self.pc_passivos_com_partes_relacionadas = float(pc_passivos_com_partes_relacionadas)
        self.pc_dividendos_e_jcp_a_pagar = float(pc_dividendos_e_jcp_a_pagar)
        self.pc_outros = float(pc_outros)
        self.pc_provisoes = float(pc_provisoes)
        self.pc_passivos_sobre_ativos_nao_correntes_a_venda_e_descontinuados = float(pc_passivos_sobre_ativos_nao_correntes_a_venda_e_descontinuados)
        self.pc_outros = float(pc_outros)
        self.passivo_nao_circulante_ = float(passivo_nao_circulante_)
        self.pnc_emprestimos_e_financiamentos = float(pnc_emprestimos_e_financiamentos)
        self.pnc_passivos_com_partes_relacionadas = float(pnc_passivos_com_partes_relacionadas)
        self.pnc_outros = float(pnc_outros)
        self.pnc_tributos_diferidos = float(pnc_tributos_diferidos)
        self.pnc_adiantamento_para_futuro_aumento_capital = float(pnc_adiantamento_para_futuro_aumento_capital)
        self.pnc_provisoes = float(pnc_provisoes)
        self.pnc_passivos_sobre_ativos_nao_correntes_a_venda_e_descontinuados = float(pnc_passivos_sobre_ativos_nao_correntes_a_venda_e_descontinuados)
        self.pnc_lucros_e_receitas_a_apropriar = float(pnc_lucros_e_receitas_a_apropriar)
        self.pnc_participacao_dos_acionistas_nao_controladores = float(pnc_participacao_dos_acionistas_nao_controladores)
        self.patrimonio_liquido = float(patrimonio_liquido)
        self.pl_capital_social_realizado = float(pl_capital_social_realizado)
        self.reservas_de_capital = float(reservas_de_capital)
        self.pl_reservas_de_reavaliacao = float(pl_reservas_de_reavaliacao)
        self.pl_reservas_de_lucros = float(pl_reservas_de_lucros)
        self.pl_lucros_prejuizos_acumulados = float(pl_lucros_prejuizos_acumulados)
        self.pl_ajustes_de_avaliacao_patrimonial = float(pl_ajustes_de_avaliacao_patrimonial)
        self.pl_ajustes_acumulados_de_conversao = float(pl_ajustes_acumulados_de_conversao)
        self.pl_outros_resultados_abrangentes = float(pl_outros_resultados_abrangentes)
        self.pl_adiantamento_para_futuro_aumento_capital = float(pl_adiantamento_para_futuro_aumento_capital)
