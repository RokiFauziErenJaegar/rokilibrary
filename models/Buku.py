from odoo import api, fields, models


class Buku(models.Model):
    _name = 'rokilibrary.buku'
    _description = 'New Description'

    name = fields.Char(string='Nama Buku')
    genrebuku_id = fields.Many2one(comodel_name='rokilibrary.genrebuku', string='Genre Buku')
    tgl_terbit = fields.Date(string='Tanggal Terbit')
    penerbit_id = fields.Many2one(comodel_name='rokilibrary.publisher', string='Penerbit')
    jml_halaman = fields.Integer(string='Jumlah Halaman')
    stok = fields.Integer(string='Jumlah Buku Tersedia')
    detailpeminjaman_ids = fields.One2many(comodel_name='rokilibrary.detailpeminjaman', inverse_name='buku_id', string='Detail Peminjaman')
    coverbuku = fields.Binary()
    