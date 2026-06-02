# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if self._is_sulfuras(item):
                continue

            self._update_quality_before_sell_date(item)
            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                self._update_quality_after_sell_date(item)

    def _update_quality_before_sell_date(self, item):
        if self._is_aged_brie(item):
            self._increase_quality(item, 1)
            return
        if self._is_backstage(item):
            self._increase_quality(item, 1)
            if item.sell_in <= 10:
                self._increase_quality(item, 1)
            if item.sell_in <= 5:
                self._increase_quality(item, 1)
            return

        self._decrease_quality(item, 1)
        if self._is_conjured(item):
            self._decrease_quality(item, 1)

    def _update_quality_after_sell_date(self, item):
        if self._is_aged_brie(item):
            self._increase_quality(item, 1)
            return
        if self._is_backstage(item):
            item.quality = 0
            return

        self._decrease_quality(item, 1)
        if self._is_conjured(item):
            self._decrease_quality(item, 1)

    def _increase_quality(self, item, amount):
        item.quality = min(50, item.quality + amount)

    def _decrease_quality(self, item, amount):
        item.quality = max(0, item.quality - amount)

    def _is_aged_brie(self, item):
        return item.name == "Aged Brie"

    def _is_backstage(self, item):
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def _is_sulfuras(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"

    def _is_conjured(self, item):
        return item.name.startswith("Conjured")


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
